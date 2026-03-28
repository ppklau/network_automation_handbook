# Network Automation Business Case Template

**Organisation:**
**Prepared by:**
**Date:**
**Version:**
**Sponsor:**

---

## Executive Summary

> *[2–4 sentences. State what is being requested, what it will deliver, and the investment required. Write for a reader who will go no further than this paragraph.]*
>
> Example: "This business case requests investment of [£X] over 18 months to transform ACME Investments' network operations from a largely manual function to an automated, platform-based model. The programme will reduce change-related outages by an estimated 75%, cut connectivity lead times from 15 days to same-day, and eliminate the manual audit preparation effort currently consuming 3 weeks of senior engineering time per regulatory review. The investment returns within 14 months."

---

## 1. Current-State Cost

*Quantify what the current state costs. Use real data from your organisation wherever possible.*

### Change Operations

| Metric | Current Value | Source |
|---|---|---|
| Network changes processed per month | | Change management system |
| Average elapsed lead time per change (days) | | Change management system |
| Percentage of engineer time on routine execution | | Estimate / time study |
| Senior engineer fully-loaded cost (annual) | | HR / Finance |
| **Estimated annual cost of routine execution** | | Calculated |

### Incident Cost

| Metric | Current Value | Source |
|---|---|---|
| Change-related incidents per quarter | | Incident management system |
| Average business impact per P1 incident (£) | | Business / Finance estimate |
| Average MTTR for change-related incidents (hours) | | Incident records |
| **Estimated annual incident cost attributable to manual change** | | Calculated |

### Compliance Cost

| Metric | Current Value | Source |
|---|---|---|
| Regulatory reviews per year | | Compliance calendar |
| Engineering days consumed per review (evidence preparation) | | Engineering estimate |
| Fully-loaded daily cost of engineering resource | | HR / Finance |
| **Estimated annual compliance preparation cost** | | Calculated |

### Total Estimated Current-State Cost

| Category | Annual Cost |
|---|---|
| Routine execution (recoverable capacity) | |
| Change-related incidents | |
| Compliance preparation | |
| **Total addressable cost** | |

---

## 2. Target-State Value

*Project the value delivered at each transformation phase. Use conservative estimates.*

### Value by Pillar

| Value Pillar | Initiative | Metric | Conservative Target | Financial Value |
|---|---|---|---|---|
| Cost Reduction | Routine execution automation | Engineering hours recovered | 40% reduction by Phase 2 | |
| Risk Reduction | Pre-deployment validation + rollback | Change-related incidents | 75% reduction by Phase 2 | |
| Risk Reduction | Automated audit evidence | Compliance preparation time | Eliminated by Phase 2 | |
| Agility | One-touch deployment | Lead time: standard changes | 10 days → same day (Phase 3) | |
| Agility | Self-service portal | % requests without manual intervention | 60% by Phase 3 | |
| Service Quality | Automated detection + faster triage | MTTR for P1 incidents | 50% reduction by Phase 2 | |

### Cumulative Value Projection

| Phase | Cumulative Investment | Cumulative Value Delivered | Net Position |
|---|---|---|---|
| End of Phase 1 (Month 3) | | | |
| End of Phase 2 (Month 6) | | | |
| End of Phase 3 (Month 12) | | | |
| Month 18 | | | |
| Month 24 | | | |

**Estimated payback period:** _____ months

---

## 3. Investment Required

*Be specific. Vague investment requests lose in budget reviews.*

### People Investment

| Role | Effort | Duration | Cost |
|---|---|---|---|
| Automation architect | | | |
| Automation engineer(s) | | | |
| Product / programme management | | | |
| Training and upskilling | | | |
| **People subtotal** | | | |

### Tooling Investment

| Category | Tool/Platform | Licensing Model | Annual Cost |
|---|---|---|---|
| Source of truth | | | |
| Version control / CI platform | | | |
| Workflow orchestration | | | |
| Observability | | | |
| **Tooling subtotal** | | | |

### Total Investment by Phase

| Phase | People | Tooling | Programme Mgmt | Phase Total |
|---|---|---|---|---|
| Phase 1 — Foundation | | | | |
| Phase 2 — Scale | | | | |
| Phase 3 — Platform | | | | |
| **Total** | | | | |

---

## 4. The Cost of Inaction

*The most important section for leadership. Quantify the ongoing cost of not transforming.*

### Monthly Cost of Continued Manual Operations

| Category | Monthly Cost | Basis |
|---|---|---|
| Engineering capacity consumed by routine execution | | |
| Expected monthly cost of change-related incidents | | Historical average |
| Compliance preparation (amortised monthly) | | Annual cost ÷ 12 |
| **Total monthly cost of inaction** | | |

**At current trajectory, over 18 months of delay, the cost of inaction is approximately: [£X]**

*This is the financial case for beginning Phase 1 immediately rather than deferring.*

### Risk Trajectory

> *[Describe how the risk profile changes over time if no action is taken. Examples: growing team dependency on a small number of individuals, increasing regulatory scrutiny, business agility constrained as competitors invest in automation, technical debt accumulation.]*

---

## 5. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Phase 1 scope creep extends foundation phase | Medium | Medium | Hard scope boundary; dedicated phase owner |
| Skills gap limits delivery pace | Medium | High | Skills assessment in month 1; upskilling plan before Phase 2 |
| Change management process blocks automated deployment | Medium | High | Engage change management stakeholder before Phase 1 begins |
| Leadership commitment wavers during Phase 2 | Low | High | Monthly stakeholder updates with business metrics; Phase 1 win demonstrated early |
| Automation adoption lower than expected | Medium | Medium | Automation ambassador programme; feedback mechanism from Phase 1 |

---

## 6. Governance and Accountability

| Element | Detail |
|---|---|
| **Programme sponsor** | |
| **Programme lead** | |
| **Investment approval body** | |
| **Progress review cadence** | Monthly (stakeholder update) + quarterly (roadmap review) |
| **Success criteria for Phase 1** | See [Phase Milestone Checklist](roadmap-phase-milestones.md) |
| **Decision to proceed to Phase 2** | Phase 1 exit criteria met + sponsor sign-off |

---

## 7. Recommendation

> *[One paragraph. State clearly what you are recommending and why. Avoid hedging.]*
>
> Example: "We recommend approval of Phase 1 investment of [£X] to begin immediately, with a Phase 2 decision gate at Month 3 subject to Phase 1 exit criteria being met. The cost of delay — [£Y] per month — exceeds the cost of programme initiation. The programme has a conservative payback period of [Z] months and delivers material risk reduction, compliance simplification, and business agility improvements that are not achievable through any other initiative currently under consideration."

---

## Appendix: Supporting Data

*Attach or reference: incident logs, change management reports, time study results, regulatory review evidence, engineering team capacity analysis.*
