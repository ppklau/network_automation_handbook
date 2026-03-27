# 13 — Dashboards & Reporting

## Purpose

Provide a standardised dashboard model for tracking transformation progress and operational health. Dashboards align stakeholders, demonstrate value, and sustain executive support.

## Audience

- **Primary:** Network Infrastructure Leaders, Transformation Leads
- **Secondary:** Engineering teams (for operational metrics)

## Content Outline

### Why Dashboards Matter
- Track transformation progress across maturity levels
- Align all stakeholders around shared metrics
- Provide transparency and sustain executive support
- Demonstrate continuous progress (small wins compound)

### Three Required Views

#### Executive View
- Automation adoption % (what percentage of eligible changes go through automation)
- MTTR reduction (trending over time)
- Change success rate
- Cost savings (operational hours recovered, incident reduction)

#### Engineering View
- Pipeline success rate
- Test coverage (what percentage of intents have automated verification)
- Deployment frequency
- Percentage of eligible changes executed via automation
- Cycle time from request to production

#### Operations View
- Incident auto-resolution rate
- Alert noise reduction
- Drift detected vs remediated
- MTTD (mean time to detect)

### Metrics Framework
- Aligned with product thinking article's three categories:
  - **Adoption:** unique users, workflow volume, automation coverage
  - **Quality & Reliability:** success rates, MTTR, change failure rate
  - **Business Impact:** incident reduction, outage minutes, audit effort, time-to-deliver

### Deliverables
- Sample dashboard architecture
- Example metrics schema
- Guide to implement with common observability platforms
- Monthly value summary template

## Cross-References

- [02 — Business Alignment](../02-business-alignment/) — the value pillars dashboards track
- [03 — Maturity Model](../03-maturity-model/) — KPIs per maturity level
- [04 — Transformation Roadmap](../04-transformation-roadmap/) — milestone tracking
- [08 — Operations Automation](../08-operations-automation/) — operational metrics sources

## Source Articles

- [Why Network Automation Needs Product Thinking](https://ppklau.github.io/article/why_network_automation_needs_product_thinking/)

## Status

`draft` — content to be developed
