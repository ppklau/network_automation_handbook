# Auto-Remediation Risk Register

## About This Template

The auto-remediation risk register is the governance document for your automation's decision-making authority. It records every category of drift or fault that the automation layer is authorised to act on, the conditions under which it may act, and the tier of action permitted.

This register should be reviewed quarterly and updated whenever the automation scope changes. Changes to tier assignments should be approved by the automation programme owner.

**The register does two things:**
1. Explicitly authorises specific automated actions (reducing ambiguity about what automation is allowed to do)
2. Explicitly excludes automation from specific scenarios (creating a documented boundary that operations teams and auditors can rely on)

---

## Register Summary

| Organisation | [Organisation name] |
|---|---|
| Environment scope | [Production / All environments / Specific segments] |
| Register version | [v1.0] |
| Last reviewed | [YYYY-MM] |
| Approved by | [Role / name] |
| Next review | [YYYY-MM] |

**Tier definitions:**

| Tier | Action | Criteria |
|---|---|---|
| 1 | Auto-remediate without human approval | Low risk, fully reversible, root cause deterministic, automation validated |
| 2 | Propose remediation, require approval | Moderate risk, human judgement needed for context or timing |
| 3 | Alert only — do not act | High risk, unknown root cause, or automation not yet validated |
| 4 | Never automate | Structural risk, compliance requirement, or irreversible action |

---

## Risk Register Entries

### Section 1: Routing

| ID | Scenario | Tier | Permitted Action | Hard Stops | Runbook | Notes |
|---|---|---|---|---|---|---|
| REM-RTG-01 | BGP session down (single peer) | 1 | Clear BGP session; verify re-establishment | Multiple sessions down simultaneously; session down > 30 min | RB-BGP-01 | — |
| REM-RTG-02 | BGP session down (multiple peers) | 3 | Alert only — page on-call | — | RB-BGP-02 | Multiple peers may indicate upstream or hardware issue |
| REM-RTG-03 | OSPF adjacency loss (single neighbour) | 2 | Propose: restart OSPF process | Multiple adjacencies affected; topology change in last 4h | RB-OSPF-01 | — |
| REM-RTG-04 | Prefix leak detected (route appearing in wrong VRF) | 3 | Alert only | — | RB-RTG-03 | Requires human investigation of policy |
| REM-RTG-05 | Routing black hole detected | 4 | Never automate | — | RB-RTG-04 | Root cause investigation required; automated action risks compounding the fault |

---

### Section 2: Connectivity

| ID | Scenario | Tier | Permitted Action | Hard Stops | Runbook | Notes |
|---|---|---|---|---|---|---|
| REM-CON-01 | Interface flapping (>3 state changes in 5 min) | 2 | Propose: err-disable interface | Core/uplink interfaces; port-channel members | RB-INT-01 | — |
| REM-CON-02 | Port-channel member down | 3 | Alert only | — | RB-LAG-01 | Port-channel resilience masks single member failures; investigation required |
| REM-CON-03 | Interface utilisation > 90% sustained 15 min | 2 | Propose: traffic engineering adjustment | — | RB-INT-02 | Requires human decision on rerouting |
| REM-CON-04 | MTU mismatch detected | 3 | Alert only | — | RB-INT-03 | Configuration change required; use pipeline |

---

### Section 3: Management Plane

| ID | Scenario | Tier | Permitted Action | Hard Stops | Runbook | Notes |
|---|---|---|---|---|---|---|
| REM-MGMT-01 | Configuration drift from SoT | 1 | Re-apply SoT configuration (merge mode) | Drift on >3 devices simultaneously; drift on security ACLs; production change window not open | RB-DRIFT-01 | Pipeline-driven remediation only |
| REM-MGMT-02 | SNMP polling failure (device unreachable) | 2 | Propose: verify management plane connectivity | — | RB-MGMT-01 | — |
| REM-MGMT-03 | NTP drift > 5 seconds | 1 | Re-sync NTP; verify stratum | — | RB-MGMT-02 | — |
| REM-MGMT-04 | Syslog forwarding gap > 15 min | 2 | Propose: restart syslog process | — | RB-MGMT-03 | — |
| REM-MGMT-05 | SSH connectivity loss to device | 3 | Alert only | — | RB-MGMT-04 | May indicate broader management plane failure |

---

### Section 4: Security

| ID | Scenario | Tier | Permitted Action | Hard Stops | Runbook | Notes |
|---|---|---|---|---|---|---|
| REM-SEC-01 | ACL hit rate spike (>10x baseline) | 3 | Alert only — notify security team | — | RB-SEC-01 | Security events require human triage |
| REM-SEC-02 | Management plane access from unexpected source IP | 3 | Alert only | — | RB-SEC-02 | — |
| REM-SEC-03 | Security ACL change detected outside pipeline | 4 | Never automate | — | RB-SEC-03 | Out-of-band ACL changes require immediate human investigation; automated response risks masking a security incident |
| REM-SEC-04 | New BGP peer announcement from untrusted AS | 4 | Never automate | — | RB-SEC-04 | Requires security and routing team joint review |

---

### Section 5: Hardware and Platform

| ID | Scenario | Tier | Permitted Action | Hard Stops | Runbook | Notes |
|---|---|---|---|---|---|---|
| REM-HW-01 | Interface CRC error rate > threshold | 3 | Alert only — flag for hardware review | — | RB-HW-01 | — |
| REM-HW-02 | Transceiver receive power below threshold | 3 | Alert only | — | RB-HW-02 | Hardware replacement required |
| REM-HW-03 | CPU utilisation > 80% sustained 10 min | 3 | Alert only | — | RB-HW-03 | Root cause investigation required |
| REM-HW-04 | Memory utilisation > 85% | 3 | Alert only | — | RB-HW-04 | — |
| REM-HW-05 | Power supply failure | 3 | Alert only — page on-call | — | RB-HW-05 | Physical intervention required |

---

## Tier 4 — Permanently Excluded from Automation

The following actions are permanently excluded from automated execution, regardless of how well the root cause is understood. Record the reason explicitly.

| Scenario | Reason for permanent exclusion |
|---|---|
| Security ACL removal or permissive rule addition | Regulatory requirement (MiFID II / FCA SYSC) — all firewall/ACL changes require human authorisation |
| BGP policy modification | Routing policy changes have wide blast radius; human architectural review required |
| VRF creation or deletion | Cross-zone routing implication; requires security and architecture approval |
| Any configuration change on border/edge devices | Highest risk — requires change control and senior approval |
| Firmware or OS upgrade | Non-reversible; requires maintenance window and human oversight |
| [Add additional exclusions] | [Reason] |

---

## Adding a New Entry

Before adding a new Tier 1 entry, all of the following must be true:

- [ ] Root cause is deterministic — the same trigger always has the same root cause
- [ ] The remediation action is fully reversible
- [ ] The action has been validated in a lab or staging environment
- [ ] The automation has run in dry-run mode in production for at least 30 days without false positives
- [ ] The hard stops are explicitly defined
- [ ] A runbook exists for the manual equivalent
- [ ] The entry has been reviewed and approved by the automation programme owner

**Promotion path:** Tier 3 (observe) → Tier 2 (propose, validate judgement) → Tier 1 (auto-act)

New categories should start at Tier 3. Promotion to Tier 2 requires 30 days of alert-only observation with documented confirmation that alert conditions correctly identify the target scenario. Promotion to Tier 1 requires 60 days at Tier 2 with approval rate > 95% and zero cases where an approval was later judged incorrect.

---

## Governance

| Review trigger | Action |
|---|---|
| Quarterly review | Validate all Tier 1 entries against recent incident data; check hard stops are still sufficient |
| Auto-remediation acted incorrectly | Immediate review — demote to Tier 2 or 3 pending investigation |
| New device type added to estate | Review which entries apply; may require validation period before Tier 1 status |
| Regulatory change | Review all security-related entries |
| Post-incident review | Check whether automation should have acted differently |

**Approval authority for tier changes:**

| Change | Required approval |
|---|---|
| Tier 3 → Tier 2 | Automation lead |
| Tier 2 → Tier 1 | Automation programme owner + operations lead |
| Any → Tier 4 | Automation programme owner |
| Tier 4 → any lower | Automation programme owner + CISO/security lead |
