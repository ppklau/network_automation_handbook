# Maturity Assessment Questionnaire

Use this questionnaire during the working group phase of the assessment workshop. For each dimension, work through the questions as a group. Base your score on evidence — specific examples from recent experience — not general impressions.

**Scoring guide:**
- Score to the *lower* level when evidence is mixed or practice is not consistent across the team
- "We intend to..." or "we are planning to..." does not count as current capability
- If you are debating between two levels, score the lower one

---

## Dimension 1: Change Execution

> How are network changes made today?

**Questions:**

1. Walk through the last non-trivial change your team made. What did the end-to-end process look like?
2. How many people were involved, and what tools did they use?
3. Could any engineer on the team have executed that change in the same way? Or did it depend on specific individuals?
4. Is there a defined, documented process that all engineers follow for standard change types?
5. Are changes version-controlled? Is there an audit trail of what changed, when, and by whom?

**Scoring indicators:**

| Level | Evidence |
|---|---|
| 1 | Changes made manually via CLI, no documented process, no audit trail beyond change tickets |
| 2 | Some changes automated via scripts; scripts not shared or standardised |
| 3 | Standard change types have documented, version-controlled automation; most engineers can execute |
| 4 | All changes flow through a pipeline with automated validation; no direct manual execution in production |
| 5 | Changes are intent-driven; engineers specify outcomes, system determines and applies configuration |

**Agreed score:** ___ **Evidence:**

---

## Dimension 2: Knowledge and Documentation

> Where does operational knowledge live today?

**Questions:**

1. If your three most experienced engineers left tomorrow, what operational knowledge would be lost?
2. How do new engineers learn how the network is designed and how to make changes?
3. Is there a single authoritative record of what the network is supposed to look like?
4. How long would it take to produce an accurate list of all devices, their configurations, and their roles?
5. When documentation exists, how current is it? When was it last updated?

**Scoring indicators:**

| Level | Evidence |
|---|---|
| 1 | Knowledge is in people's heads; documentation is sparse, outdated, or not trusted |
| 2 | Some documentation exists; some engineers maintain personal notes or scripts |
| 3 | A source of truth exists and is actively maintained; configuration is version-controlled |
| 4 | Source of truth is the system of record; automation reads from it; human-managed exceptions are rare |
| 5 | Intent model serves as the source of truth; device configuration is derived, not directly maintained |

**Agreed score:** ___ **Evidence:**

---

## Dimension 3: Consistency and Repeatability

> Do the same inputs reliably produce the same outputs?

**Questions:**

1. Does the same type of change always produce the same outcome, regardless of who handles it?
2. Are there change types where the outcome depends on individual knowledge or judgement?
3. How do you detect when a device's actual configuration has drifted from its intended configuration?
4. How often does drift occur? What causes it?
5. When drift is detected, what is the remediation process?

**Scoring indicators:**

| Level | Evidence |
|---|---|
| 1 | Outcomes vary by engineer; no mechanism to detect or prevent drift |
| 2 | Some standardisation in specific areas; inconsistency remains common |
| 3 | Standard processes exist; outcomes are consistent for covered change types; drift detection in place |
| 4 | Automated validation ensures consistency; drift is detected and flagged automatically |
| 5 | Continuous compliance enforcement; drift triggers automatic remediation |

**Agreed score:** ___ **Evidence:**

---

## Dimension 4: Speed and Lead Time

> How long does it actually take to deliver a change?

**Questions:**

1. What is the average elapsed time from a connectivity request being raised to it being delivered?
2. Break that time down: how much is queue time or waiting for approvals, versus active engineering work?
3. What is the fastest you have ever delivered a significant change? What made that possible?
4. What would need to change to make that exceptional speed routine?
5. Are there change types where lead time is consistently under one hour? What makes those different?

**Scoring indicators:**

| Level | Evidence |
|---|---|
| 1 | Lead time 10+ days; dominated by queue time and manual effort |
| 2 | Some improvement for scripted change types; inconsistent overall |
| 3 | Standard changes delivered in hours to a day; process is defined and predictable |
| 4 | Standard changes delivered in under an hour; same-day complex changes routinely achieved |
| 5 | Near-instant for automated change types; human involvement only for novel or high-risk changes |

**Agreed score:** ___ **Evidence:**

---

## Dimension 5: Testing and Validation

> How do you know a change is safe before it reaches production?

**Questions:**

1. What testing or validation occurs before a change is deployed to production?
2. Is that testing automated or manual?
3. How are potential side-effects of a change identified before deployment?
4. What is the rollback process when a change causes an unexpected problem? How long does it take?
5. Have automated tests ever caught a problem that manual review missed? Give an example.

**Scoring indicators:**

| Level | Evidence |
|---|---|
| 1 | No pre-deployment testing; changes validated in production; rollback is manual and slow |
| 2 | Ad-hoc testing by individual engineers; no standardised pre-production validation |
| 3 | Defined testing steps exist; peer review is standard; some automated checks |
| 4 | Automated testing pipeline; changes validated in a virtual/staging environment before production |
| 5 | Intent validation is continuous; automated testing covers all change types; rollback is automatic |

**Agreed score:** ___ **Evidence:**

---

## Dimension 6: Compliance and Audit Readiness

> How readily can you demonstrate that controls are working?

**Questions:**

1. How would you demonstrate to a regulator that all network changes over the past quarter were authorised, tested, and correctly implemented?
2. How long would it take to compile that evidence?
3. Are security policies enforced automatically, or do they depend on engineers following documented procedures?
4. How would you detect if a security control had been disabled or misconfigured?
5. Is compliance evidence generated as a by-product of normal operations, or does it require a separate effort?

**Scoring indicators:**

| Level | Evidence |
|---|---|
| 1 | Evidence is manual; audit preparation takes weeks; compliance depends on individual behaviour |
| 2 | Partial records in change management system; still significant manual effort to compile |
| 3 | Version control and change records provide a basic audit trail; some automation of evidence |
| 4 | Pipeline generates compliance evidence automatically; policies enforced by guardrails, not procedure |
| 5 | Continuous compliance state; real-time policy enforcement; audit evidence always current |

**Agreed score:** ___ **Evidence:**

---

## Dimension 7: Consumer Experience

> How do the teams that depend on the network experience working with it?

**Questions:**

1. How do application or platform teams request network changes?
2. What feedback do you receive from those teams about responsiveness and predictability?
3. Are there workarounds in place because the network cannot move fast enough?
4. Can consuming teams get any network resource without raising a manual request?
5. How would you know if a consuming team was frustrated with the current process?

**Scoring indicators:**

| Level | Evidence |
|---|---|
| 1 | All requests via ticket queue; no self-service; consuming teams wait weeks; workarounds common |
| 2 | Some faster paths for known request types; still largely manual and ticket-driven |
| 3 | Standard request types handled consistently and within defined SLAs; feedback loop exists |
| 4 | Self-service available for common change types; consuming teams can access resources via API or portal |
| 5 | Infrastructure largely invisible to consumers; network adapts to workload needs automatically |

**Agreed score:** ___ **Evidence:**

---

## Scoring Summary

Transfer agreed scores here at the end of the working group session.

| Dimension | Agreed Level | Key Gap |
|---|---|---|
| Change Execution | | |
| Knowledge & Documentation | | |
| Consistency & Repeatability | | |
| Speed & Lead Time | | |
| Testing & Validation | | |
| Compliance & Audit | | |
| Consumer Experience | | |

**Overall assessment:**

**Headline strength:**

**Most important gap:**

**Notes for readout:**
