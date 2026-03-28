# Roadmap Phase Milestone Checklist

Use these checklists as exit criteria for each phase. A phase is complete when all mandatory items are checked and the phase review has been signed off by the programme sponsor.

**Note:** These are the minimum conditions for completing a phase — not a ceiling. Add organisation-specific items as needed.

---

## Phase 1 — Foundation

**Exit criteria: the organisation now has a demonstrated, repeatable, trustworthy automated workflow and the infrastructure to build more.**

### Technology
- [ ] Source of truth established for at least one domain (structured, version-controlled, maintained)
- [ ] All automation code and configuration templates are in a shared version-controlled repository
- [ ] No automation scripts remain on individual laptops or personal drives
- [ ] Basic CI pipeline runs on every commit: linting, syntax validation, and policy checks
- [ ] At least one change type is executed end-to-end via automation with pre-deployment validation
- [ ] Rollback mechanism tested and confirmed to work

### Process
- [ ] Change management process updated to recognise automated pipeline as an approved execution path
- [ ] Peer review process defined for automation code (merge request, review criteria, approval gates)
- [ ] Incident response runbook updated to reflect automated deployment patterns

### People
- [ ] All team members have access to and understand the version control repository
- [ ] At least two engineers (not just one) can operate and extend the automated workflow
- [ ] Onboarding documentation exists for the automation environment

### Metrics
- [ ] Baseline metrics recorded: lead time, change success rate, manual vs automated change ratio
- [ ] Measurement mechanism in place (automated where possible, manual otherwise)

### Stakeholder
- [ ] Phase 1 outcomes demonstrated to programme sponsor
- [ ] Consuming teams aware of the automated workflow and its capabilities
- [ ] Phase 2 scope agreed and backlog prioritised

---

## Phase 2 — Scale

**Exit criteria: automation is an organisational discipline, covering the majority of routine change volume, with cross-team workflows and visible metrics.**

### Technology
- [ ] Automation coverage: ≥50% of routine change types executed via pipeline
- [ ] Policy-as-code implemented for agreed security and compliance policies
- [ ] Pipeline catches policy violations before production deployment (verified by test cases)
- [ ] Workflow orchestration in place for at least two cross-team change types
- [ ] Configuration drift detection operational and alerting

### Process
- [ ] Standard operating procedure exists for each automated change type
- [ ] Exception handling process defined: what happens when the pipeline fails?
- [ ] Compliance evidence generated automatically for audit-relevant changes
- [ ] Change management process updated to support higher deployment frequency

### People
- [ ] Automation ambassadors identified and enabled in at least two consuming teams
- [ ] Skills gap assessment completed for Phase 3 requirements
- [ ] Platform ownership explicitly assigned with dedicated capacity (not best-efforts)

### Metrics
- [ ] Observability dashboard operational (engineering view minimum)
- [ ] Deployment frequency, change failure rate, and pipeline success rate visible in near real-time
- [ ] Consumer satisfaction feedback mechanism in place

### Stakeholder
- [ ] Monthly stakeholder update delivered with metrics evidence
- [ ] Phase 2 outcomes presented to senior leadership
- [ ] Phase 3 scope agreed and investment confirmed

---

## Phase 3 — Platform

**Exit criteria: the network operates as a platform; consuming teams can provision defined resources without raising manual tickets; one-touch deployment is operational for templated infrastructure.**

### Technology
- [ ] One-touch deployment operational for at least one infrastructure template (branch, segment, or connectivity domain)
- [ ] Self-service interface available for consuming teams (portal, API, or ITSM integration)
- [ ] Intent-based service model defined and implemented for at least one service type
- [ ] Closed-loop remediation operational for at least one incident class
- [ ] Full pipeline coverage for all standard change types (target: ≥80%)

### Process
- [ ] Self-service consumption process documented and communicated to all eligible consuming teams
- [ ] Guardrails defined and implemented: what self-service can and cannot do
- [ ] Escalation process defined for requests outside self-service scope
- [ ] SLA published for automated versus self-service versus manual request types

### People
- [ ] Engineering team capacity model updated to reflect platform operations model
- [ ] Consuming team onboarding process documented and tested
- [ ] Network engineering roles updated to reflect shift from execution to platform management

### Metrics
- [ ] Self-service utilisation rate tracked
- [ ] Lead time for one-touch deployment measured and reported
- [ ] Pipeline bypass rate tracked and under agreed threshold

### Stakeholder
- [ ] One-touch deployment demonstrated to business stakeholders
- [ ] Business outcome improvements quantified and communicated (lead time, cost, compliance)
- [ ] Phase 4 direction agreed; specific use cases identified

---

## Phase 4 — Adaptive

**Phase 4 does not have a fixed exit criteria — it is a continuous improvement mode. Use these indicators to assess progress.**

### Progress Indicators
- [ ] Intent-driven configuration generation operational for at least one domain
- [ ] AI-assisted anomaly detection in production with documented false positive rate
- [ ] Self-healing operational for defined incident classes; success rate measured and reported
- [ ] Continuous compliance enforcement operational: violations detected and remediated automatically
- [ ] MTTD for in-scope incident classes below defined threshold
- [ ] Engineering capacity allocation: majority of time on intent design and platform evolution, not execution

### Ongoing Disciplines
- [ ] Quarterly roadmap review conducted; backlog updated based on findings
- [ ] ADR register maintained: all significant decisions recorded
- [ ] Metrics reviewed monthly; anomalies investigated
- [ ] Consumer feedback incorporated into platform backlog regularly
