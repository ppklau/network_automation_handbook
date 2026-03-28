# Business Requirement Traceability Template

Use this template to trace each business requirement through to its technical implementation and measurement. Maintain one entry per significant requirement. This document is the primary bridge between business stakeholders and the engineering team — it makes design decisions auditable and justification explicit.

**Organisation:**
**Owner:**
**Last reviewed:**

---

## How to Use This Template

Each requirement follows a four-link chain:

1. **Business Requirement** — what the business needs, in business terms, without reference to technology. Must be traceable to a specific stakeholder or business outcome.
2. **Design Intent** — what the network must do to meet that requirement. Architectural commitment, not implementation detail.
3. **Technical Implementation** — the specific capability, pattern, or change that delivers the design intent. Tool and architecture choices appear here.
4. **KPI / Measurement** — the metric that confirms the requirement is being met and demonstrates value to the stakeholder.

Complete all four links before beginning technical implementation. If you cannot complete the KPI row, the requirement is not yet well enough defined to build against.

---

## Requirement Register

### REQ-001: [Requirement Name]

| Link | Content |
|---|---|
| **Business Requirement** | |
| **Stakeholder / Source** | |
| **Design Intent** | |
| **Technical Implementation** | |
| **KPI** | Metric: &nbsp;&nbsp; Baseline: &nbsp;&nbsp; Target: |
| **Status** | Not started / In progress / Delivered |
| **Phase** | Phase 1 / 2 / 3 / 4 |

---

### REQ-002: [Requirement Name]

| Link | Content |
|---|---|
| **Business Requirement** | |
| **Stakeholder / Source** | |
| **Design Intent** | |
| **Technical Implementation** | |
| **KPI** | Metric: &nbsp;&nbsp; Baseline: &nbsp;&nbsp; Target: |
| **Status** | Not started / In progress / Delivered |
| **Phase** | Phase 1 / 2 / 3 / 4 |

---

### REQ-003: [Requirement Name]

| Link | Content |
|---|---|
| **Business Requirement** | |
| **Stakeholder / Source** | |
| **Design Intent** | |
| **Technical Implementation** | |
| **KPI** | Metric: &nbsp;&nbsp; Baseline: &nbsp;&nbsp; Target: |
| **Status** | Not started / In progress / Delivered |
| **Phase** | Phase 1 / 2 / 3 / 4 |

---

*(Add further requirements as needed)*

---

## Traceability Matrix

A consolidated view for review with leadership. Update after each phase.

| Req ID | Business Requirement (summary) | Value Pillar | Phase | KPI | Current vs Target |
|---|---|---|---|---|---|
| REQ-001 | | Cost / Risk / Agility / Quality | | | |
| REQ-002 | | Cost / Risk / Agility / Quality | | | |
| REQ-003 | | Cost / Risk / Agility / Quality | | | |

---

## ACME Investments — Example Entries

### REQ-001: MiFID II Audit Trail

| Link | Content |
|---|---|
| **Business Requirement** | All network changes must be fully auditable and traceable to an authorised requester. Evidence must be available on demand without manual assembly. |
| **Stakeholder / Source** | Head of Compliance / FCA SYSC 10A |
| **Design Intent** | Every configuration change is version-controlled, peer-reviewed, and pipeline-validated. The pipeline generates a complete audit record including requester, approver, validation result, diff, and deployment timestamp. |
| **Technical Implementation** | GitLab CI pipeline with merge request approval gates. Automated diff generation. Structured pipeline logs exported to SIEM. All changes committed to Git with attribution. |
| **KPI** | Metric: audit evidence preparation time &nbsp;&nbsp; Baseline: 3 weeks per regulatory review &nbsp;&nbsp; Target: on-demand, zero manual effort |
| **Status** | Phase 2 — In progress |
| **Phase** | Phase 2 |

---

### REQ-002: Faster Trading Venue Onboarding

| Link | Content |
|---|---|
| **Business Requirement** | New trading venue connectivity must be available within one business day of commercial agreement. Current lead time is 15 days. |
| **Stakeholder / Source** | Head of Electronic Trading / Business Development |
| **Design Intent** | Trading zone connectivity follows a templated pattern. A new venue requires parameterisation of a known template, not bespoke design. All dependencies are automated within a single workflow. |
| **Technical Implementation** | `generate_venue.py` generates the full configuration set from a structured specification. Batfish validates result against existing topology model. Pipeline deploys on approval. |
| **KPI** | Metric: lead time from commercial agreement to live connectivity &nbsp;&nbsp; Baseline: 15 days &nbsp;&nbsp; Target: same-day |
| **Status** | Phase 3 — Not started |
| **Phase** | Phase 3 |
