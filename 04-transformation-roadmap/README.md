# 04 — Transformation Roadmap

## Purpose

Translate the maturity assessment into a phased, actionable transformation plan. The roadmap is the training plan — it builds capabilities progressively, across technology, process, people, and business alignment.

## Audience

- **Primary:** Network Infrastructure Leaders, Transformation Leads
- **Secondary:** Automation Architects, Engineering Managers

## Content Outline

### From Assessment to Roadmap
- The maturity assessment provides the starting point
- The roadmap defines the path to the target state
- Target state defined by capabilities, not tools

### The Four Pillars of Transformation
- **Technology:** platforms, pipelines, tooling
- **Process:** workflows, change management, CI/CD
- **People:** skills, team structures, culture
- **Business Alignment:** stakeholder engagement, metrics, value demonstration

### Product Thinking for the Roadmap
- Treat the roadmap as a product backlog, not a fixed plan
- Phased delivery with measurable milestones
- Reprioritise based on adoption, risk, and measurable value
- Extends: [Why Network Automation Needs Product Thinking](https://ppklau.github.io/article/why_network_automation_needs_product_thinking/)

### Example Phased Roadmap

#### Phase 1: Foundation (0–3 months)
- MVP: one workflow, end-to-end, with validation and rollback
- Source of truth for one domain
- Version control and basic CI pipeline
- Baseline metrics established

#### Phase 2: Scale (3–6 months)
- Expand automation coverage
- Policy-as-code for ACLs
- Workflow orchestration for cross-team dependencies
- Observability dashboards

#### Phase 3: Platform (6–12 months)
- One-touch deployment capability
- Intent-based service modelling
- Self-service portals
- Closed-loop remediation for low-risk scenarios

#### Phase 4: Adaptive (12+ months)
- Intent-driven generation
- Automated design verification
- AI-assisted operations
- Self-healing capabilities

### Decision Making and Governance
- Architecture Decision Records (ADRs)
- Clear decision-making processes to maintain momentum
- Documenting rationale preserves context for future teams

### Measuring Progress
- Percentage of changes via automation
- Deployment frequency
- Change failure rate
- Lead time for changes

## Cross-References

- [03 — Maturity Model](../03-maturity-model/) — the assessment that feeds the roadmap
- [05 — Tooling Strategy](../05-tooling-strategy/) — buy vs build decisions for each phase
- [10 — People & Skills](../10-people-and-skills/) — the human side of each phase
- [templates/executive/](../templates/executive/) — roadmap presentation template

## Source Articles

- [From Maturity Model to Roadmap](https://ppklau.github.io/article/netdevops_maturity_model_to_roadmap/)
- [Why Network Automation Needs Product Thinking](https://ppklau.github.io/article/why_network_automation_needs_product_thinking/)

## Status

`draft` — content to be developed
