# 03 — Maturity Model

## Purpose

Provide a structured framework for assessing an organisation's current network automation maturity. The maturity model is the foundation — everything else in the handbook builds on knowing where you stand today.

## Audience

- **Primary:** Network Infrastructure Leaders, Automation Architects
- **Secondary:** All stakeholders participating in the assessment

## Content Outline

### Why Assess Maturity First
- "Before running a marathon, understand your current health"
- Assessment creates shared understanding across teams
- Anchors the transformation in real operational outcomes, not tool adoption

### Business Outcomes Mapping
- Reliability & resilience
- Speed & agility
- Cost efficiency
- Risk & compliance
- Every improvement maps to one or more of these outcomes

### The Five Maturity Levels

#### Level 1: Reactive
- Manual operations, tribal knowledge, ticket-driven
- Lead time for change: 10+ days
- Change success rate: <85%

#### Level 2: Task-Based Automation
- Ad-hoc scripting, scripts on individual laptops
- Automation coverage: <20%
- Inconsistent outcomes depending on who handles the task

#### Level 3: Integrated Workflows
- Source of truth introduced, standardised automation, version control
- Repeatable processes, consistent outcomes regardless of engineer
- Configuration drift detection

#### Level 4: Network as a Platform
- CI/CD pipelines, automated testing, workflow orchestration
- One-touch deployment, self-service capabilities
- Lead time for change: <1 hour
- Deployment frequency: multiple times per day

#### Level 5: Adaptive / Intent-Based
- Closed-loop automation, intent-driven, auto-deployment
- AI-assisted observability, self-healing
- MTTD: near zero
- Engineers govern intent; machines handle configuration

### How to Run a Maturity Assessment
- Structured cross-functional workshop
- Gather stakeholders (including sceptics)
- Identify operational pain points
- Define desired business outcomes
- Map current capabilities to maturity levels
- Map a real workflow through the levels

### Assessment Output
- Shared understanding of current state
- Identified capability gaps
- Input to the transformation roadmap (Chapter 04)

## Cross-References

- [04 — Transformation Roadmap](../04-transformation-roadmap/) — translates assessment into action
- [02 — Business Alignment](../02-business-alignment/) — business outcomes framework
- [13 — Dashboards](../13-dashboards/) — KPIs per maturity level

## Source Articles

- [NetDevOps Maturity Model: Health Assessment for Your Network](https://ppklau.github.io/article/netdevops_maturity_model_health_ssessment_for_your_network/)

## Status

`draft` — content to be developed
