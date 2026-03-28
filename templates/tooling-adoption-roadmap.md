# Tooling Adoption Roadmap

Track tool adoption decisions and status across each transformation phase. Update as decisions are made and deployments progress.

**Organisation:**
**Last updated:**
**Owner:**

---

## Phase 1 — Foundation

Target: minimal viable toolchain to support one end-to-end automated workflow.

| Category | Decision | Tool / Approach | Status | Owner | Notes |
|---|---|---|---|---|---|
| Source of Truth | | YAML in Git (recommended start) | Not started / Evaluating / Decided / Deployed | | |
| Version Control | | GitHub / GitLab (follow org standard) | | | |
| Automation Framework | | Ansible / Nornir | | | |
| CI/CD Pipeline | | GitLab CI / GitHub Actions (follow org standard) | | | |
| Testing — Linting | | yamllint, ansible-lint | | | Deploy from day one |
| Testing — SoT Intent | | Custom Python (build) | | | Start simple; extend with each new intent |

**Phase 1 toolchain decision date:**
**Phase 1 toolchain approved by:**

---

## Phase 2 — Scale

Target: expanded toolchain supporting broader coverage, compliance evidence, and pilot orchestration.

| Category | Decision | Tool / Approach | Status | Owner | Notes |
|---|---|---|---|---|---|
| Testing — Model-based | | Batfish | | | Add as automation coverage expands |
| Observability — Telemetry | | gNMI/SNMP + collector | | | |
| Observability — Logging | | Adopt enterprise standard | | | |
| Drift Detection | | Oxidized | | | |
| Compliance Evidence | | Pipeline artefacts + log export | | | |
| Workflow Orchestration | | Evaluate and pilot | | | Do not deploy to production in Phase 2 |

**Orchestration platform evaluated:**
**Orchestration pilot scope:**
**Orchestration production decision date (target):**

---

## Phase 3 — Platform

Target: production orchestration, potential SoT migration, post-deployment live device testing.

| Category | Decision | Tool / Approach | Status | Owner | Notes |
|---|---|---|---|---|---|
| Workflow Orchestration | | ServiceNow / Itential / StackStorm / AWX | | | Production deployment |
| Source of Truth | | Reassess: remain YAML or migrate to NetBox/Nautobot | | | |
| Testing — Live Device | | pyATS | | | Post-deployment verification for critical changes |
| Dashboarding | | Adopt enterprise standard | | | Aligned with Chapter 13 |

---

## Phase 4 — Adaptive

Target: high-fidelity telemetry for AI-assisted operations; evaluate AI/ML tooling.

| Category | Decision | Tool / Approach | Status | Owner | Notes |
|---|---|---|---|---|---|
| Telemetry | | Streaming telemetry gNMI/gRPC | | | Replace/augment SNMP polling |
| AI/ML — Anomaly Detection | | Evaluate | | | Requires telemetry data foundation |
| AI/ML — Intent Assistance | | Evaluate | | | Requires structured intent model |
| Event-driven Orchestration | | StackStorm or equivalent | | | If event-driven closed loops are in scope |

---

## Open Decisions

Decisions not yet made that are blocking or time-sensitive.

| Decision | Options | Due | Owner | Blocking |
|---|---|---|---|---|
| | | | | |
| | | | | |

---

## Decision Log

Record significant tooling decisions with rationale as they are made.

| Date | Category | Decision | Rationale | ADR Reference |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

---

## Buy vs Build Decisions

Record explicit build decisions — where the team has decided to build rather than buy/adopt — with justification.

| Capability | Decision | Justification | Owner | Review Date |
|---|---|---|---|---|
| SoT intent checks | Build | Encodes our specific design intents; no commercial product provides this | | |
| | Build | | | |
| | Build | | | |

> **Reminder:** Every component you build is a product you must support. Review build decisions annually.
