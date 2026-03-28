# Value Pillar Mapping Template

Map each automation initiative to the business value pillar(s) it addresses, the KPI that measures delivery, and the consuming stakeholder who cares most about that outcome.

Use this to:
- Prioritise the backlog by business value (not technical preference)
- Ensure every initiative has a measurable outcome
- Prepare stakeholder communication by pillar

**Organisation:**
**Date:**

---

## Value Pillars Reference

| Pillar | What It Means | Stakeholder |
|---|---|---|
| **Cost Reduction** | Lower operational overhead, reduced cost per change, freed engineer capacity, lower audit cost | CFO, Head of IT Finance |
| **Risk Reduction** | Fewer outages, faster recovery, consistent policy, reduced key-person dependency | CRO, Head of Risk, CISO |
| **Agility & Speed** | Faster delivery, shorter lead times, self-service, business not constrained by infrastructure | COO, Business leads, Application teams |
| **Service Quality** | Consistent outcomes, predictable performance, proactive fault detection, lower MTTR | COO, Operations leads, Consuming teams |

---

## Initiative Mapping

| Initiative | Phase | Primary Pillar | Secondary Pillar | KPI | Target | Stakeholder |
|---|---|---|---|---|---|---|
| Source of truth (YAML + Git) | 1 | Risk Reduction | Cost Reduction | Configuration drift incidents | Baseline → 0 | Head of Risk |
| CI/CD pipeline — first workflow | 1 | Risk Reduction | Agility | Change lead time (pilot type) | 4 days → 2 hours | Operations |
| Policy-as-code (ACLs) | 2 | Risk Reduction | — | Policy violations caught pre-production | Baseline | CISO |
| Automated audit evidence | 2 | Cost Reduction | Risk Reduction | Audit prep time per review | 3 weeks → hours | Compliance |
| Workflow orchestration | 2 | Agility | Service Quality | Cross-team change lead time | Baseline | Application teams |
| Observability dashboard | 2 | Service Quality | — | MTTD for network anomalies | Baseline | Operations |
| One-touch deployment | 3 | Agility | Cost Reduction | Lead time: templated infra | Weeks → hours | Business leads |
| Self-service portal | 3 | Agility | Service Quality | % requests via self-service | 0% → 60% | Application teams |
| Closed-loop remediation | 3 | Service Quality | Risk Reduction | Auto-resolved incidents (%) | 0% → 40% | Operations |
| Intent-based modelling | 4 | Agility | Risk Reduction | Config-to-intent compliance | Baseline → 99% | Architecture |

---

## Pillar Summary View

A consolidated view by pillar for leadership communication.

### Cost Reduction

| Initiative | Status | KPI | Current | Target |
|---|---|---|---|---|
| | | | | |

**Total engineering hours recovered to date:**
**Estimated annual value:**

---

### Risk Reduction

| Initiative | Status | KPI | Current | Target |
|---|---|---|---|---|
| | | | | |

**Change-related incidents per quarter (baseline vs current):**
**Compliance preparation time (baseline vs current):**

---

### Agility & Speed

| Initiative | Status | KPI | Current | Target |
|---|---|---|---|---|
| | | | | |

**Lead time for standard change (baseline vs current):**
**Lead time for templated deployment (baseline vs current):**

---

### Service Quality

| Initiative | Status | KPI | Current | Target |
|---|---|---|---|---|
| | | | | |

**MTTR for P1 incidents (baseline vs current):**
**Self-service adoption rate:**

---

## Quarterly Review Table

Use this table in stakeholder updates. Update each quarter.

| Pillar | Last Quarter Delivery | KPI Movement | Next Quarter Focus |
|---|---|---|---|
| Cost Reduction | | | |
| Risk Reduction | | | |
| Agility & Speed | | | |
| Service Quality | | | |
