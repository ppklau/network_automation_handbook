# 7.4 — Deployment Patterns

The deployment stage is where validated configuration changes reach production devices. The decisions made here — how configurations are applied, how failures are handled, how blast radius is controlled — directly determine the risk profile of the automation pipeline.

---

## Replace vs Merge: The Fundamental Decision

Every deployment involves one of two models for applying configuration to a device.

### Merge (incremental) deployment

The candidate configuration is compared to the running configuration. Only the delta — the lines that differ — is applied. Lines not in the candidate are left unchanged on the device.

```
Running config:   interface Ethernet1
                    description "uplink to spine01"
                    ip address 10.0.1.1/31

Candidate config: interface Ethernet1
                    description "uplink to spine01 (updated)"
                    ip address 10.0.1.1/31

Applied delta:    interface Ethernet1
                    description "uplink to spine01 (updated)"
```

**Advantages:** Conservative and safe for incremental changes. Does not touch configuration that was not part of the intended change. Well-suited for changes to a running production device where only a subset of configuration is being modified.

**Disadvantage:** Configuration drift accumulates. Lines that exist on the device but are not in the source of truth are never removed. Over time, the device's running configuration diverges from the source of truth — it has everything in the SoT, plus whatever accumulated before the automation was in place.

**When to use:** Incremental changes to existing devices — adding VLANs, updating ACL entries, modifying routing policy. Phase 1 and Phase 2 of the transformation, when the SoT does not yet represent the full device configuration.

### Replace (full) deployment

The candidate configuration completely replaces the running configuration. The device ends up in exactly the state described by the SoT — nothing more, nothing less.

```
Running config:   ! legacy config from before automation
                  spanning-tree mode rapid-pvst
                  ! hand-added by engineer in 2023
                  no ip proxy-arp
                  interface Ethernet1
                    description "uplink to spine01"

Candidate config: interface Ethernet1
                    description "uplink to spine01"
                    ip address 10.0.1.1/31

Result:           interface Ethernet1
                    description "uplink to spine01"
                    ip address 10.0.1.1/31
                  (legacy config removed; hand-added config removed)
```

**Advantage:** The device's running state always matches the source of truth exactly. No drift accumulation. The source of truth is genuinely the source of truth.

**Disadvantage:** Requires a complete, correct representation of the device in the SoT before replace mode can be safely used. Applying a replace to a device whose SoT entry is incomplete will remove configuration that the device needs.

**When to use:** New device provisioning (the SoT is the complete config from the start). Mature deployments where the SoT fully represents the device. Scheduled remediation runs to eliminate accumulated drift.

**ACME's approach:** Merge mode for incremental changes in Phase 1 and Phase 2. Targeted replace for new device provisioning. Scheduled replace runs on Sundays for the DC fabric, after the SoT was confirmed to fully represent the device configuration at the end of Phase 2.

---

## Blast Radius Containment

Blast radius is the scope of a deployment failure. A deployment that modifies 50 devices has a larger blast radius than one that modifies 5 — and requires different controls.

### Change scope limitation

The pipeline should enforce a maximum number of devices modified per deployment run. For ACME, the default limit is 10 devices per pipeline run. Changes affecting more than 10 devices require a separate approval flag that acknowledges the expanded scope.

```yaml
# In deploy.py — blast radius check
MAX_DEVICES_DEFAULT = 10
MAX_DEVICES_EXTENDED = 50   # requires explicit flag

def check_blast_radius(devices_to_modify: list, extended: bool = False) -> None:
    limit = MAX_DEVICES_EXTENDED if extended else MAX_DEVICES_DEFAULT
    if len(devices_to_modify) > limit:
        raise BlastRadiusError(
            f"Change affects {len(devices_to_modify)} devices "
            f"(limit: {limit}). Use --extended-blast-radius flag "
            f"to override with explicit acknowledgement."
        )
```

### Canary deployment

For changes affecting many devices — a routing policy update that touches all leaf switches, for example — deploy to a subset first and verify before proceeding.

```
Phase 1: Deploy to leaf01, leaf02 (canary — 2 of 8 leaves)
         → Run post-deploy verification
         → Wait 5 minutes; observe telemetry
Phase 2: If Phase 1 passes, deploy to remaining 6 leaves
         → Run post-deploy verification
```

The canary group should be representative but non-critical — not the switches directly serving the most sensitive workloads. For ACME, the canary group is always `leaf01` and `leaf02`, which serve development and test workloads in the trading zone, not production execution engines.

Canary deployment is not built into every pipeline run — it is a deployment mode invoked for high-risk change types. The `.gitlab-ci.yml` configuration includes a `CANARY_DEPLOY` variable that enables this mode.

### Site-by-site sequencing

For changes that span multiple sites — a management policy update that applies to all branch offices, for example — deploy site by site rather than all sites simultaneously:

```
Batch 1: lon-branch1 (pilot site — familiar, well-monitored)
         → Verify, approve
Batch 2: ams-branch1, par-branch1
         → Verify, approve
Batch 3: remaining branches
```

This limits the blast radius of a configuration error to one site while the change is still in its early stages, and limits the blast radius of a partial failure to the batch in progress.

---

## Rollback Strategy

Automatic rollback is non-negotiable in a production automation pipeline. The cost of a partial deployment that leaves devices in an inconsistent state — some on the new configuration, some on the old — is higher than the cost of a clean rollback to the previous state.

### Pre-deployment snapshot

Before any deployment begins, the pipeline captures the current configuration of all target devices and stores it as a pipeline artefact. This is the rollback target.

```python
def pre_deploy_snapshot(devices: list, output_dir: str) -> None:
    """
    Capture running configuration from all target devices before deployment.
    Stored as pipeline artefact; used as rollback target if deployment fails.
    """
    for device in devices:
        conn = napalm.get_network_driver(device.platform)(
            hostname=device.hostname,
            username=os.environ['DEPLOY_USERNAME'],
            password=os.environ['DEPLOY_PASSWORD']
        )
        conn.open()
        config = conn.get_config(retrieve='running')['running']
        with open(f"{output_dir}/{device.hostname}_pre_deploy.cfg", 'w') as f:
            f.write(config)
        conn.close()
```

### Automatic rollback on failure

If any device deployment fails, the pipeline rolls back all devices that were modified in the current run:

```python
def deploy_with_rollback(devices: list, generated_dir: str,
                         snapshot_dir: str) -> None:
    deployed = []
    try:
        for device in devices:
            deploy_device(device, generated_dir)
            deployed.append(device)
    except DeploymentError as e:
        logger.error(f"Deployment failed on {e.device}: {e}")
        logger.info(f"Rolling back {len(deployed)} deployed devices")
        for d in reversed(deployed):   # rollback in reverse order
            rollback_device(d, snapshot_dir)
        raise
```

The rollback applies the pre-deployment snapshot — restoring the device to exactly the state it was in before the pipeline ran. This is deterministic; there is no guesswork about what state to target.

### Manual rollback procedure

Automatic rollback handles deployment failures. Operational rollbacks — where a change was successfully deployed but produced unexpected effects discovered post-deployment — require a different mechanism.

The standard manual rollback procedure:
1. The change that introduced the problem is identified (from pipeline history)
2. The MR that introduced the change is reverted (a Git revert, creating a new commit)
3. The revert MR goes through the same pipeline as any other change — lint, verify intents, Batfish, approval, deploy
4. The pipeline deploys the reverted configuration

This procedure is slower than automatic rollback but is the appropriate mechanism for operational issues that are discovered after the change has been in production for some time. It maintains the governance discipline — the revert is reviewed and validated before deployment.

---

## Napalm Deployment Patterns

ACME uses Napalm for device deployment. The relevant patterns:

**Merge mode (incremental):**
```python
driver = napalm.get_network_driver('eos')
device = driver(hostname=hostname, username=user, password=pwd)
device.open()
device.load_merge_candidate(filename=config_file)
diff = device.compare_config()   # review before committing
if diff:
    device.commit_config()
else:
    device.discard_config()       # nothing to do
device.close()
```

**Replace mode (full):**
```python
device.load_replace_candidate(filename=config_file)
diff = device.compare_config()   # critical to review before replace
# Replace is destructive — confirm diff is expected before committing
device.commit_config()
```

**The diff review is mandatory.** Before `commit_config()` is called, the diff is stored as a pipeline artefact and reviewed by the approval gate. An unexpected diff — one that removes more configuration than intended — is a signal to discard rather than commit.

---

## Idempotency

All deployment operations must be idempotent. Running the deployment pipeline twice against a device that is already in the target state should produce no changes — not partial re-applies, not duplicate configuration entries, not error messages.

Idempotency is a property of the deployment tooling (Napalm handles this for configuration management) and a property of the templates (templates must not generate configuration that is sensitive to ordering or accumulates on re-application).

Test idempotency explicitly: run the deployment pipeline against a device, then immediately run it again without modifying the SoT. The second run should produce an empty diff and apply zero changes.

---

*Continue to: [One-Touch Deployment](../one-touch-deployment/chapter.md)*
