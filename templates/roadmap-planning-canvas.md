# Transformation Roadmap Planning Canvas

Use this canvas to plan your four-phase transformation roadmap. Complete one column per phase. Start with Phase 1 only — complete subsequent phases as you gain experience and validate your direction.

**Organisation:**
**Date:**
**Facilitator:**

---

## Business Context (Complete Before Phasing)

**Target maturity level (18-month horizon):**

**Top 3 business outcomes to deliver:**
1.
2.
3.

**Top 3 capability gaps from maturity assessment:**
1.
2.
3.

**Non-negotiable constraints:**
(e.g., regulatory deadlines, budget ceilings, team size limits, technology mandates)

---

## Phase Planning

### Phase 1 — Foundation

**Duration target:** 6–10 weeks
**Objective:** Prove that reliable, version-controlled automation is achievable in this organisation.

| Element | Detail |
|---|---|
| **Domain in scope** | (e.g., DC fabric VLAN provisioning — not everything) |
| **Source of truth** | What system? What data? Who maintains it? |
| **Version control** | Platform, branching model, review process |
| **First automated workflow** | Which change type? What does end-to-end mean? |
| **Validation approach** | How is the change verified before and after deployment? |
| **Rollback mechanism** | What happens if deployment fails? |
| **Baseline metrics to capture** | Lead time, manual vs automated %, change success rate |
| **Exit criteria** | What must be true before Phase 2 begins? |

**Key risks:**

**Owner:**

---

### Phase 2 — Scale

**Duration target:** 3–6 months
**Objective:** Extend Phase 1 disciplines across more change types and stakeholders.

| Element | Detail |
|---|---|
| **Additional change types** | Which change types are next in the backlog? |
| **Coverage target** | % of routine changes via pipeline (target: 50–60%) |
| **Policy-as-code scope** | Which policies will be encoded and enforced in pipeline? |
| **Workflow orchestration** | Which cross-team changes need coordination? How? |
| **Observability** | What dashboards? What metrics? (See Chapter 13) |
| **Consuming team engagement** | Which teams? What do they need? Who are the ambassadors? |
| **Exit criteria** | What must be true before Phase 3 begins? |

**Key risks:**

**Owner:**

---

### Phase 3 — Platform

**Duration target:** 6–12 months
**Objective:** Make the network a platform consumed through well-defined interfaces.

| Element | Detail |
|---|---|
| **One-touch deployment scope** | Which templated infrastructure types? What triggers deployment? |
| **Self-service interface** | Portal, API, ITSM integration, or combination? |
| **Intent model scope** | What services will be modelled at intent level? |
| **Closed-loop scope** | Which incident types will be auto-remediated? |
| **Consuming team enablement** | How will teams be onboarded to self-service? |
| **Exit criteria** | What must be true before Phase 4 begins? |

**Key risks:**

**Owner:**

---

### Phase 4 — Adaptive

**Duration target:** 12+ months (ongoing)
**Objective:** Move from defined workflow automation to continuous intent enforcement and adaptive operations.

| Element | Detail |
|---|---|
| **Intent model expansion** | Which additional services/domains? |
| **AI/ML use cases** | Anomaly detection, predictive fault, observability — what specifically? |
| **Self-healing scope** | What incident classes? What remediation logic? |
| **Continuous compliance scope** | What policies enforced continuously? |
| **Success measure** | How will you know Phase 4 is delivering value? |

**Key risks:**

**Owner:**

---

## Dependency Map

Record dependencies between phases and between initiatives within phases.

| Capability | Depends On | Phase |
|---|---|---|
| CI/CD pipeline | Source of truth | P1 → P1 |
| Policy-as-code | Version control + CI pipeline | P1 → P2 |
| Self-service portal | Automated pipeline + workflow orchestration | P2 → P3 |
| One-touch deployment | Source of truth + templated workflows | P2 → P3 |
| Intent modelling | Source of truth + pipeline + self-service | P3 → P3/4 |
| AI-assisted operations | High-quality telemetry (P2+) + labelled data | P2+ → P4 |
| | | |
| | | |

---

## Prioritisation Matrix

Plot Phase 2+ initiatives here to guide sequencing decisions.

```
                    HIGH FEASIBILITY
                           │
            QUICK WINS     │    STRATEGIC PRIORITIES
                           │
LOW IMPACT ────────────────┼──────────────────── HIGH IMPACT
                           │
            DEFER/DROP     │    INVEST TO ENABLE
                           │
                    LOW FEASIBILITY
```

**Quick Wins:**

**Strategic Priorities:**

**Invest to Enable (blockers):**

**Defer/Drop:**

---

## Investment Summary (Indicative)

| Phase | People | Tooling | Programme Management | Total (Indicative) |
|---|---|---|---|---|
| Phase 1 | | | | |
| Phase 2 | | | | |
| Phase 3 | | | | |
| Phase 4 | | | | |

---

## Governance Cadence

| Mechanism | Frequency | Owner | Attendees |
|---|---|---|---|
| Roadmap review | Quarterly | | |
| Stakeholder update | Monthly | | |
| Engineering retrospective | Fortnightly | | |
