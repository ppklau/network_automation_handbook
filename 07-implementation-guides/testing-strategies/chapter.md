# 7.3 — Testing Strategies

Automated testing is what gives the pipeline its authority. Without it, the pipeline is a deployment mechanism. With it, it is a governance mechanism — capable of asserting that every proposed change conforms to every stated design intent before any device is touched.

This guide covers the testing taxonomy, the two-layer verification architecture used in ACME's pipeline, and the practical decisions that determine how comprehensive your test coverage becomes over time.

---

## The Testing Taxonomy

Network automation testing spans six distinct layers. Each layer asks different questions, operates at different speeds, and catches different classes of error. They are complementary, not interchangeable.

```
Layer                  What It Checks              Speed     When It Runs
──────────────────────────────────────────────────────────────────────────
1. Lint / Syntax       Structure, formatting        Seconds   Every commit
2. Schema Validation   Data model conformance       Seconds   Every commit
3. SoT Intent Checks   Design intent compliance     Seconds   Every commit
4. Template Unit Tests Template rendering           Seconds   Every commit
5. Model-based (Batfish) Network behaviour          Minutes   Every MR
6. Post-deploy (pyATS) Live device state            Minutes   After deployment
```

### Layer 1: Lint and Syntax

The cheapest test: is the file valid? `yamllint` checks YAML formatting and structure. `ansible-lint` checks playbook quality. JSON Schema validation checks that `nodes.yml` conforms to the expected schema.

These tests run in seconds and should block the pipeline immediately on failure. There is no benefit in proceeding to Batfish validation if `nodes.yml` contains a syntax error.

### Layer 2: Schema Validation

Distinct from linting — schema validation checks that the data model conforms to the declared structure. A `nodes.yml` file can be syntactically valid YAML and still fail schema validation if a required field is missing or a value is of the wrong type.

A JSON Schema or Pydantic model defines the expected structure of each device record. The schema validator runs against the full `nodes.yml` and reports every violation. This is the first layer of defence against data model drift.

### Layer 3: SoT Intent Verification

The most important custom layer. `verify_intents.py` reads both `design_intents.yml` and `nodes.yml` and asserts that the data model structurally satisfies every design intent.

This layer is custom — it encodes ACME's specific design standards. No commercial product can write these checks for you, because they express your organisation's architectural commitments, not generic best practices.

The ACME intent verification suite runs 12 checks:

```
Running 12 intent checks...

  [PASS] INTENT-TOPO-01: Spine-leaf fabric exists
  [PASS] INTENT-TOPO-02: MLAG on all leaf pairs
  [PASS] INTENT-TOPO-03: VXLAN VNI=VLAN on all leaves
  [PASS] INTENT-RTG-01: eBGP underlay, unique ASNs
  [PASS] INTENT-RTG-02: eBGP EVPN enabled on all nodes
  [PASS] INTENT-RTG-03: OSPF area 0 at branch sites
  [PASS] INTENT-SEG-01: VRF per zone, no cross-zone leakage
  [PASS] INTENT-SEG-02: ACLs: deny-default, comments, no any
  [PASS] INTENT-SEG-03: DMZ VLANs only in DMZ VRF
  [PASS] INTENT-MGMT-01: OOB management VRF on all nodes
  [PASS] INTENT-MGMT-02: Syslog x2 + SNMPv3 on all nodes
  [PASS] INTENT-IP-01: All IPs within declared zone prefix

Results: 12 passed, 0 failed out of 12
```

Each check is a Python function that inspects the data model and raises an assertion error with a descriptive message on failure. The check for `INTENT-SEG-02` is representative of the level of detail:

```python
def check_intent_seg_02(nodes: list, intents: dict) -> None:
    """
    INTENT-SEG-02: ACLs enforce zone policy at leaf ingress.
    - Every ACL must have default_action: deny
    - Every ACL entry must have a comment containing a REQ- reference
    - No ACL may contain a permit-any rule
    """
    for node in nodes:
        for acl in node.get('acls', []):
            # Check default deny
            assert acl.get('default_action') == 'deny', \
                f"{node['hostname']}: ACL {acl['name']} missing default deny"

            for entry in acl.get('entries', []):
                # Check requirement reference in comment
                comment = entry.get('comment', '')
                assert re.search(r'REQ-\w+-\d+', comment), \
                    f"{node['hostname']}: ACL {acl['name']} seq {entry['seq']} "
                    f"missing requirement reference in comment"

                # Check no permit-any
                if entry.get('action') == 'permit':
                    src = entry.get('src', '')
                    dst = entry.get('dst', '')
                    assert not (src == 'any' and dst == 'any'), \
                        f"{node['hostname']}: ACL {acl['name']} seq {entry['seq']} "
                        f"contains permit-any rule (violates INTENT-SEG-02)"
```

This check is not aspirational — it is executable. If an engineer adds an ACL entry without a requirement reference, or with a permit-any rule, the pipeline fails with a specific error message before any configuration is rendered.

### Layer 4: Template Unit Tests

Each Jinja2 template is tested by rendering it against a known input fixture and comparing the output against an expected result file:

```python
def test_arista_leaf_template():
    """Render the Arista EOS leaf template and verify output."""
    input_data = load_fixture('fixtures/leaf01_input.yml')
    expected_output = load_fixture('fixtures/leaf01_expected.cfg')

    rendered = render_template('templates/arista_eos/leaf.j2', input_data)

    assert rendered.strip() == expected_output.strip(), \
        "Leaf template output differs from expected:\n" + \
        unified_diff(expected_output, rendered)
```

Template unit tests catch regressions when the schema changes, when Jinja2 filter behaviour changes, or when a template modification has unintended side-effects on other device types. They are fast (milliseconds per template) and should run on every commit.

### Layer 5: Model-Based Testing (Batfish)

Batfish operates on rendered configurations. It builds a complete network model — all devices, all routing protocols, all ACLs — and answers behavioural questions about that model.

The distinction from Layer 3: SoT intent verification checks the data; Batfish checks the behaviour of the rendered configuration. A SoT that declares the correct intent can still produce a misconfigured device if the template has a bug. Batfish catches the misconfiguration.

ACME's `batfish_validate.py` runs the following assertion categories:

**Reachability assertions:**
```python
# Trading zone MUST NOT reach DMZ without firewall traversal
result = bf.q.reachability(
    pathConstraints=PathConstraints(
        startLocation="/trading_.*/",
        endLocation="/dmz_.*/"
    ),
    actions="DELIVERED_TO_SUBNET"
).answer()
assert len(result.frame()) == 0, \
    "Trading zone can reach DMZ without firewall — INTENT-SEG-01 violation"

# Management plane MUST reach all devices via MGMT VRF
result = bf.q.reachability(
    pathConstraints=PathConstraints(
        startLocation="mgmt_server",
        endLocation="/.*/"
    ),
    ingressInterface="eth0"
).answer()
assert len(result.frame()) == total_devices, \
    f"Management plane cannot reach all devices — INTENT-MGMT-01 violation"
```

**Routing correctness:**
```python
# No routing loops
loops = bf.q.detectLoops().answer()
assert loops.frame().empty, f"Routing loops detected: {loops.frame()}"

# All BGP sessions reach Established
bgp_sessions = bf.q.bgpSessionStatus().answer()
non_established = bgp_sessions.frame()[
    bgp_sessions.frame()['Established_Status'] != 'ESTABLISHED'
]
assert non_established.empty, \
    f"BGP sessions not Established: {non_established[['Node','Remote_Node']]}"
```

**Blast radius analysis:**
```python
# For the specific change being reviewed, what paths change?
# This helps reviewers understand the impact of the proposed change
diff = bf.q.differentialReachability(
    snapshot=proposed_snapshot,
    reference=current_snapshot
).answer()
# Store as artefact for reviewer inspection
diff.frame().to_json('reports/blast_radius.json')
```

### Layer 6: Post-Deployment Verification

After deployment, a lightweight verification suite confirms that the deployment had the intended effect on the live devices. This is not a full Batfish re-run — it is a targeted check of the specific changes applied.

For ACME, post-deployment checks include:
- BGP session state on modified devices (sessions should be Established)
- VLAN existence on leaf switches where VLANs were added
- Management plane connectivity (SSH accessible on expected VRF)
- ACL existence and entry count on modified switches

If pyATS is deployed, this stage runs the relevant test suite against the modified devices using the pyATS Genie parsers to extract structured state and assert against expectations.

---

## JUnit XML and Pipeline Integration

All test layers should emit JUnit XML output. GitLab CI and GitHub Actions both render JUnit XML natively as test reports — each test appears as a named test case in the pipeline UI, with pass/fail status and error messages.

The value of JUnit integration:
- Failed tests appear by name in the MR, not as opaque pipeline failures
- Test history is tracked across pipeline runs — regressions are visible
- Test reports are stored as pipeline artefacts alongside the compliance evidence

The JUnit output from the ACME pipeline, for a failed `INTENT-SEG-02` check, looks like this in the GitLab MR:

```
❌ INTENT-SEG-02: ACLs enforce zone policy at leaf ingress
   FAILED: leaf03: ACL ACL_TRADING_IN seq 30 missing requirement
   reference in comment
   Expected: comment containing REQ-XXXX-XX
   Got: "temporary allow for testing"
```

The engineer sees immediately what failed, on which device, and why. No log diving required.

---

## Building Test Coverage Over Time

Test coverage should grow with automation coverage. Every new design intent added to `design_intents.yml` should have a corresponding check in `verify_intents.py`. Every new template should have a unit test fixture.

A useful heuristic: if a design decision is important enough to encode as a design intent, it is important enough to verify automatically. The two artefacts — the intent definition and the verification check — should be created together, in the same merge request.

**The regression protection principle:** Every incident or compliance finding that was caused by a configuration error should result in a new test that would have caught it. The test suite grows to protect against known failure modes. Over time, this creates a safety net that reflects the organisation's actual operational experience — not a generic checklist.

---

*Continue to: [Deployment Patterns](../deployment-patterns/chapter.md)*
