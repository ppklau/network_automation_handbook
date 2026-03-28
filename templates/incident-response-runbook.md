# Incident Response Runbook Template

## About This Template

Use this template to create runbooks for automated or semi-automated incident response. Each runbook should cover a single, well-defined incident type. Runbooks are executed by the operations automation layer; they are also the documentation that engineers use when automation is unavailable or the incident falls outside automation scope.

---

## Runbook: [Incident Type Name]

**Runbook ID:** `RB-[CATEGORY]-[NUMBER]` (e.g., `RB-BGP-01`)
**Category:** [Routing / Connectivity / Management Plane / Hardware / Security / Performance]
**Automation tier:** [Tier 1 — Auto-remediate / Tier 2 — Propose and approve / Tier 3 — Alert only]
**Last reviewed:** [YYYY-MM]
**Owner:** [Team or role]

---

## 1. Incident Description

**What this covers:** [One paragraph describing the incident type. Be specific — "BGP session down" not "routing problem".]

**Examples:**
- [Specific example scenario 1]
- [Specific example scenario 2]

**Explicitly out of scope:** [Scenarios that look similar but are handled by a different runbook.]

---

## 2. Detection

**Primary alert:** [Alert name / monitoring rule that triggers this runbook]

**Alert conditions:**
```
[Alert definition — threshold, duration, source]
Example: BGP session state != Established for > 2 minutes on any peer
```

**Secondary signals:** [Additional telemetry that supports the diagnosis — interface counters, system logs, SNMP traps]

**False positive rate:** [Low / Medium / High — and the conditions that cause false positives]

---

## 3. Automated Diagnostics

Steps the automation layer runs before escalating or remediating:

| Step | Action | Expected Output | Failure Condition |
|---|---|---|---|
| 1 | [Diagnostic action] | [What success looks like] | [What triggers escalation] |
| 2 | [Diagnostic action] | [What success looks like] | [What triggers escalation] |
| 3 | [Diagnostic action] | [What success looks like] | [What triggers escalation] |

**Diagnostic script / tool:** `[script name or command]`

**Data collected:**
- [Piece of telemetry or state collected]
- [Piece of telemetry or state collected]
- [Piece of telemetry or state collected]

---

## 4. Classification Logic

How the automation layer decides what to do:

```
IF [condition A] AND [condition B]
  THEN → Auto-remediation (Tier 1): [Action]
ELIF [condition C]
  THEN → Propose remediation (Tier 2): [Action] — requires approval
ELIF [condition D]
  THEN → Alert and escalate (Tier 3): page on-call
ELSE
  THEN → Alert only — unknown condition, human investigation required
```

**Tier 1 criteria:** [Conditions that must all be true before auto-remediation proceeds]

**Hard stops — do not auto-remediate if:**
- [ ] [Condition that excludes auto-remediation]
- [ ] [Condition that excludes auto-remediation]
- [ ] Multiple devices affected simultaneously (may indicate broader issue)

---

## 5. Remediation Actions

### Tier 1: Automated Remediation

**Action:** [Specific remediation action]

**Pre-conditions (all must be true):**
1. [Pre-condition 1]
2. [Pre-condition 2]

**Steps:**
1. [Step 1 — what the automation does]
2. [Step 2]
3. [Step 3]
4. Verify: [What success looks like]
5. If verification fails: [Escalation action]

**Rollback:** [How to undo this action if it makes things worse]

**Script / tool:** `[script name]`

---

### Tier 2: Proposed Remediation (Requires Approval)

**Proposed action:** [What the automation suggests]

**Approval required from:** [Role or team]

**Presented to approver:**
- Diagnosis summary
- Proposed action and expected effect
- Rollback plan
- Estimated impact if not actioned

**Approval channel:** [Slack channel / ITSM ticket / ServiceNow approval workflow]

---

### Tier 3: Escalation (Alert Only)

**Page:** [On-call role]

**Alert contents:**
- Incident type and affected device(s)
- Diagnostic data collected
- Suggested first investigation steps
- Link to this runbook

**Escalation path:** [Primary → Secondary → Management]

---

## 6. Manual Remediation Procedure

For use when automation is unavailable or the incident does not match automated classification:

1. **Verify the incident**
   ```
   [Verification command or check]
   ```

2. **Gather state**
   ```
   [Commands to run on affected device]
   ```

3. **Check recent changes**
   - Review pipeline artefacts for changes deployed in the last 24 hours
   - Check ITSM change log for scheduled changes

4. **Remediation steps**
   ```
   [Manual remediation steps]
   ```

5. **Verify remediation**
   ```
   [Verification commands]
   ```

6. **Document**
   - Update the ITSM incident ticket with root cause and resolution
   - If a pipeline artefact caused the incident, raise a bug against the relevant SoT entry

---

## 7. Post-Incident

**Incident closed when:** [Specific condition — not "when it feels resolved"]

**Actions:**
- [ ] Update ITSM ticket with root cause
- [ ] If auto-remediation triggered: review automation log and verify expected behaviour
- [ ] If auto-remediation failed or missed: update runbook with new classification condition
- [ ] If a configuration change caused the incident: create ADR or SoT schema update to prevent recurrence
- [ ] If this is a recurring incident: schedule post-mortem and blameless review

**Metrics to record:**
- Time to detect (TTD)
- Time to remediate (TTR)
- Was the incident detected by monitoring before a user reported it?
- Did automation handle it without human involvement?

---

## 8. Runbook Maintenance

| Field | Detail |
|---|---|
| Review cadence | Quarterly, or after any incident handled by this runbook |
| Review trigger | Runbook auto-remediation fails; new device type added to estate; false positive rate increases |
| Reviewer | [Operations lead / automation engineer] |
| Validation method | [How to test this runbook — lab simulation / dry-run mode] |

---

## Adaptation Guide

**Incident categories to create runbooks for:**

| Category | Example incidents |
|---|---|
| Routing | BGP session down, OSPF adjacency loss, routing black hole, prefix leak |
| Connectivity | Interface down, port-channel member failure, MTU mismatch |
| Management plane | SNMP unreachable, syslog gap, NTP drift, SSH connectivity loss |
| Hardware | Interface error rate threshold, transceiver alarm, power supply failure |
| Security | Unexpected ACL hit rate spike, management plane access from unexpected source |
| Performance | Interface utilisation threshold, CPU/memory threshold, queue drop rate |

**Tier assignment guidance:**

| Assign Tier 1 if... | Assign Tier 2 if... | Assign Tier 3 if... |
|---|---|---|
| Root cause is always the same | Root cause is known but human judgement is needed | Root cause varies or is unknown |
| Remediation is fully reversible | Remediation has moderate impact risk | Remediation risk is high |
| Single device affected | Multiple devices or services affected | Impact scope uncertain |
| Automation has proven reliable for this case | New automation — not yet validated | No proven automated fix exists |
