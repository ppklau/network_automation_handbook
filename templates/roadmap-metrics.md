# Transformation Metrics Tracking Template

Track these metrics from the start of Phase 1. The baseline values established in Phase 1 are what demonstrate progress in later phases.

**Organisation:**
**Tracking period:**
**Owner:**

---

## Core Operational Metrics

These measure whether the network operation is changing its behaviour.

| Metric | Baseline (Phase 1) | Phase 2 Target | Phase 3 Target | Current Value | Source |
|---|---|---|---|---|---|
| **Automation coverage** (% of change types via pipeline) | | ≥50% | ≥80% | | Pipeline logs |
| **Lead time — standard change** (hours, median) | | | <1 hour | | Change records |
| **Lead time — templated deployment** (hours, median) | | | <2 hours | | Pipeline logs |
| **Change failure rate** (% requiring rollback or emergency fix) | | | | | Incident records |
| **Deployment frequency** (automated deployments per week) | | | | | Pipeline logs |
| **Mean time to recover — P1 incidents** (hours) | | | | | Incident records |
| **Compliance evidence preparation** (days per audit cycle) | | | | | Engineering time records |

---

## Adoption Metrics

These measure whether the automation is being used — and whether consuming teams are getting value from it.

| Metric | How to Measure | Phase 2 Target | Phase 3 Target | Current Value |
|---|---|---|---|---|
| **Self-service utilisation rate** (% of eligible requests via self-service) | Request system data | — | ≥40% | |
| **Pipeline bypass rate** (% of changes made outside pipeline) | Change audit vs pipeline logs | <20% | <5% | |
| **Consumer satisfaction score** (NPS or simple 1–5 rating) | Quarterly survey | | | |
| **Onboarding time for new engineers** (days to first productive contribution) | HR / team records | | | |
| **Automation ambassador coverage** (% of consuming teams with active ambassador) | Programme tracking | ≥50% | ≥80% | |

---

## Business Outcome Metrics

These connect the technical programme to the business outcomes agreed in the Chapter 3 assessment. Customise the rows for your organisation's specific outcomes.

| Business Outcome | Metric | Baseline | Target | Current | Trend |
|---|---|---|---|---|---|
| **Speed & Agility** | Lead time: [specific use case] | | | | ↓ |
| **Reliability & Resilience** | MTTR: P1 network incidents | | | | ↓ |
| **Risk & Compliance** | Engineering hours: audit prep per quarter | | | | ↓ |
| **Cost Efficiency** | % engineering capacity on routine execution vs strategic work | | | | ↓ execution |
| **[Organisation-specific]** | | | | | |

---

## Metrics Review Cadence

| Review | Frequency | Audience | Format |
|---|---|---|---|
| Engineering metrics review | Weekly | Engineering team | Pipeline dashboard |
| Programme metrics review | Monthly | Programme leads + sponsors | Written update |
| Business outcome review | Quarterly | Senior leadership | Roadmap review presentation |

---

## Notes on Measurement

**Automation coverage:** Count the number of change types that can be executed via the pipeline, divided by the total number of change types in scope. Be consistent about what counts as "in scope" — otherwise this metric is easily gamed by removing change types from scope.

**Lead time:** Measure elapsed time from when the request enters the queue to when the change is verified as complete in production. Do not measure only the active engineering time — the waiting time is what the business experiences.

**Change failure rate:** A change "fails" if it requires a rollback, an emergency fix within 24 hours, or causes an incident. This metric will initially get worse as automation expands (more changes = more visibility of failures). Context this for leadership.

**Pipeline bypass rate:** This is the most important adoption metric. If engineers are bypassing the pipeline, the reason must be understood — is the pipeline too slow? Too restrictive? Untrustworthy? Bypass behaviour is a feedback signal, not just a compliance problem.

**Consumer satisfaction:** Keep this simple. A five-question survey sent quarterly to application and platform teams is sufficient. Track the trend, not the absolute score.
