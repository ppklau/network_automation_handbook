# Roadmap Presentation Template

This template provides three views of the transformation roadmap for three distinct audiences. Maintain all three — they describe the same plan at different levels of abstraction.

---

## View 1: Leadership (One Page)

*For: CTO, VP Infrastructure, COO, senior sponsors*
*Question it answers: "What are we investing in, and what will it deliver?"*
*Format: Slide or one-pager. No technical detail.*

---

### Network Automation Transformation — Programme Overview

**[Organisation Name] | [Date]**

#### What We Are Building

We are transforming network operations from manual, ticket-driven processes to an automated, platform-based model. This reduces operational risk, accelerates business delivery, and frees engineering capacity for higher-value work.

#### The Four Phases

| Phase | Timeframe | What We Deliver | Business Outcome |
|---|---|---|---|
| **1. Foundation** | Months 1–3 | Reliable, version-controlled automation for core change types | Reduced change failure rate; audit trail established |
| **2. Scale** | Months 3–6 | Automation across all routine changes; compliance evidence automated; cross-team workflows | Engineering capacity redirected; compliance cost reduced |
| **3. Platform** | Months 6–12 | One-touch deployment; self-service for consuming teams | New connectivity delivered in hours, not weeks |
| **4. Adaptive** | 12+ months | Intent-driven operations; self-healing; AI-assisted observability | Infrastructure adapts continuously; MTTD near zero |

#### Progress This Quarter

| Metric | Baseline | Current | Target (Phase [N] exit) |
|---|---|---|---|
| Lead time for standard change | | | |
| Automated change coverage | | | |
| Change failure rate | | | |
| Compliance evidence preparation time | | | |

#### Investment Required

| Category | Phase 1 | Phase 2 | Phase 3 | Notes |
|---|---|---|---|---|
| People | | | | |
| Tooling | | | | |
| Programme management | | | | |

#### Risks and Mitigations

| Risk | Mitigation |
|---|---|
| | |
| | |

---

## View 2: Architecture and Engineering Leadership

*For: Chief Architect, Engineering Manager, Automation Architect*
*Question it answers: "What are we building, in what order, and why?"*
*Format: Working document, updated quarterly.*

---

### Capability Roadmap

#### Phase 1 — Foundation

**Objective:** Prove reliable automation is achievable. Establish foundations for all subsequent phases.

**In scope:**
- Domain: [specify]
- Change types: [specify]
- Source of truth: [platform and data model]
- Pipeline: [tooling and stages]

**Out of scope (Phase 1):**
- [List explicitly to manage scope creep]

**Key architectural decisions:**
- [ADR-001: Source of truth platform selection]
- [ADR-002: Version control branching strategy]
- [ADR-003: Pipeline architecture]

**Dependencies:**
- None (this is the foundation)

**Exit criteria:** See [Phase Milestone Checklist](roadmap-phase-milestones.md)

---

#### Phase 2 — Scale

**Objective:** Extend Phase 1 disciplines across more change types and consuming teams.

**In scope:**
- Additional change types: [list from backlog]
- Policy-as-code: [which policies]
- Workflow orchestration: [which cross-team workflows]
- Observability: [which dashboards and metrics]

**Key architectural decisions:**
- [ADR-004: Policy enforcement model]
- [ADR-005: Workflow orchestration platform]

**Dependencies:**
- Phase 1 exit criteria met
- [Specific: source of truth must cover X domains before workflow orchestration is viable]

---

#### Phase 3 — Platform

**Objective:** Network as a platform — consumed through defined interfaces, not manual tickets.

**In scope:**
- One-touch deployment: [which infrastructure templates]
- Self-service: [interface type, scope, guardrails]
- Intent model: [which services, abstraction level]
- Closed-loop: [which incident classes]

**Key architectural decisions:**
- [ADR-006: Self-service interface design]
- [ADR-007: Intent abstraction level]
- [ADR-008: Closed-loop remediation scope and safeguards]

**Dependencies:**
- Phase 2 exit criteria met
- Workflow orchestration operational
- Consuming team onboarding process defined

---

#### Phase 4 — Adaptive

**Direction (not fixed scope):**
- Intent-driven configuration generation
- AI-assisted anomaly detection and observability
- Self-healing for expanded incident class
- Continuous compliance enforcement

**Prerequisites:**
- High-quality telemetry data (from Phase 2+)
- Labelled incident history for ML training
- Strong pipeline and rollback confidence from Phases 1–3

---

### Open Decisions

Decisions not yet made that are blocking or time-sensitive.

| Decision | Options | Due | Owner |
|---|---|---|---|
| | | | |

### ADR Register

| ADR | Title | Status | Date |
|---|---|---|---|
| ADR-001 | | | |
| ADR-002 | | | |

---

## View 3: Engineering Team

*For: Engineering team members*
*Question it answers: "What are we working on, and what does done look like?"*
*Format: Maintained as a living backlog in the team's project management tool. This template provides the structure.*

---

### Current Sprint / Iteration

**Sprint:** [number or dates]
**Phase:** [1 / 2 / 3 / 4]
**Sprint goal:** [One sentence describing what success looks like at end of sprint]

| Item | Owner | Status | Acceptance Criteria |
|---|---|---|---|
| | | To do / In progress / Done | |
| | | | |

### Backlog (Next 3 Sprints)

| Priority | Item | Phase | Notes |
|---|:---:|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

### Definition of Done (Programme-wide)

An item is done when:
- [ ] Code is in the shared repository (no local-only changes)
- [ ] Peer review completed and approved
- [ ] CI pipeline passes (linting, syntax, policy checks)
- [ ] Automated tests pass (where applicable)
- [ ] Documentation updated
- [ ] Change has been deployed and verified in the target environment
- [ ] Metrics impact noted (does this change a tracked metric?)

### Blocked Items

| Item | Blocker | Owner to Resolve | Due |
|---|---|---|---|
| | | | |
