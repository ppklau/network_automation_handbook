# 📘 Network Automation Handbook

**A comprehensive, end-to-end guide for organisations adopting network automation.**

---

## What This Is

The Network Automation Handbook is an open, practitioner-led guide that bridges the gap between business strategy and technical execution in network automation. It is not a tool tutorial. It is a transformation guide — covering maturity assessment, roadmap design, implementation patterns, organisational change, and the path toward intent-based, self-healing networks.

This handbook is designed for organisations at any stage of their automation journey:

- **Starting out?** Begin with the [Maturity Model](03-maturity-model/) and [Transformation Roadmap](04-transformation-roadmap/) to assess where you are and plan your path forward.
- **Already automating?** Jump to the [Implementation Guides](07-implementation-guides/) for pipeline design, testing strategies, and deployment patterns.
- **Building a business case?** The [Business Alignment](02-business-alignment/) chapter and [Executive Templates](templates/executive/) give you the frameworks to justify and track investment.
- **Thinking ahead?** The [Advanced Topics](11-advanced-topics/) section covers intent-based networking, AI-driven operations, and auto-healing networks.

---

## Who This Is For

### Primary Audiences

- **Network Infrastructure Leaders** (Directors, Heads of Network) — strategic view, KPIs, investment justification
- **Automation Architects** — reference architectures, design patterns, tooling strategy
- **Network Architects** — architecture patterns, intent-based design, greenfield principles

### Secondary Audiences

- **Automation Engineers** — hands-on implementation, templates, working examples
- **Network Engineers** — skills evolution, learning pathways, pipeline workflows
- **DevOps / Platform Engineers** — CI/CD patterns, testing frameworks, orchestration

Each chapter is multi-layered: executives can read the strategic summary, engineers can dive into the implementation detail.

---

## Handbook Structure

```
network-automation-handbook/
│
├── 00-executive-summary/           The case for network automation in one chapter
├── 01-introduction/                Scope, principles, how to use this handbook
├── 02-business-alignment/          Mapping technical initiatives to business value
├── 03-maturity-model/              NetDevOps maturity assessment (Levels 1–5)
├── 04-transformation-roadmap/      Phased roadmap from assessment to platform
├── 05-tooling-strategy/            Tool categories, trade-offs, workflow orchestration
├── 06-architecture-patterns/       Reference architectures, config-as-code patterns
├── 07-implementation-guides/       CI/CD pipelines, testing, deployment, one-touch
├── 08-operations-automation/       Monitoring, incident response, auto-remediation
├── 09-greenfield-design/           Greenfield-inspired principles for any environment
├── 10-people-and-skills/           Skills evolution, hiring vs upskilling, change mgmt
├── 11-advanced-topics/             Intent-based networking, AI ops, auto-healing
├── 12-security-compliance/         Compliance automation, audit trails, policy-as-code
├── 13-dashboards/                  Transformation tracking, metrics, reporting
├── templates/                      Executive, technical, and operational templates
├── examples/                       ACME Investments demo, intent model, Batfish pipeline
└── assets/                         Diagrams, images, supporting files
```

---

## Key Concepts

This handbook is built around several core ideas that recur throughout:

**Configuration is an output, not an input.** Engineers do not write device configuration. They define intent — structured, version-controlled statements about what the network should do — and the system generates configuration from that intent.

**Automation is a product, not a project.** Successful automation initiatives have backlogs, release cadences, user feedback loops, and adoption metrics. They are maintained and improved continuously, not delivered once and handed over.

**Every line of code you build becomes a product you must support.** Buy or adopt commodity capabilities. Build only where it creates genuine competitive advantage and your team can sustain it.

**Do not lose networking expertise while chasing automation.** Automation amplifies engineering skill — it does not replace it. Retain key SMEs, pair them with automation engineers, and build cross-functional teams.

**One-touch deployment enables business scalability.** Adding a new site should be a business decision, not an engineering project. Intent-driven generation makes this possible.

---

## Content Foundation

This handbook consolidates and extends a series of published articles:

| Article | Chapter(s) |
|---------|------------|
| [AI and Network Automation: A Pragmatic View for Finance Network Leaders](https://ppklau.github.io/article/ai_and_network_automation_for_finance_leaders/) | 02, 10, 11 |
| [Why Network Automation Needs Product Thinking](https://ppklau.github.io/article/why_network_automation_needs_product_thinking/) | 04, 08, 13 |
| [Using AI as a Learning Partner](https://ppklau.github.io/article/using_ai_as_a_learning_partner/) | 10, 11 |
| [What Anduril Teaches Us About Software Mindset](https://ppklau.github.io/article/what_anduril_teaches_us_about_software_mindset/) | 02, 09 |
| [NetDevOps Maturity Model: Health Assessment](https://ppklau.github.io/article/netdevops_maturity_model_health_ssessment_for_your_network/) | 03 |
| [From Maturity Model to Roadmap](https://ppklau.github.io/article/netdevops_maturity_model_to_roadmap/) | 04 |
| [Automated Network Testing with Batfish](https://ppklau.github.io/article/automated_testing_in_network_automation/) | 07 |
| [Network Configuration As Code](https://ppklau.github.io/article/network_configuration_as_code/) | 06, 07 |
| [From Commands to Intent (Part 1 of 3)](https://ppklau.github.io/article/intent_based_networking_part1/) | 06, 11 |
| Encoding Intent: A Practical Guide to Network-as-Code (Part 2 of 3) | 06, 07, 11, 12 |
| The Self-Provisioning Network (Part 3 of 3) | 07, 09, 11 |

See [article-index.md](article-index.md) for the full mapping between published articles and handbook chapters.

---

## Getting Started

### Reading Path: Executives & Leaders

1. [Executive Summary](00-executive-summary/) — the business case in 10 minutes
2. [Business Alignment](02-business-alignment/) — mapping automation to cost, risk, agility, quality
3. [Maturity Model](03-maturity-model/) — assess your current state
4. [Transformation Roadmap](04-transformation-roadmap/) — plan the journey
5. [Dashboards](13-dashboards/) — track progress and demonstrate value

### Reading Path: Engineers & Architects

1. [Architecture Patterns](06-architecture-patterns/) — reference architectures and config-as-code
2. [Implementation Guides](07-implementation-guides/) — pipelines, testing, deployment
3. [Tooling Strategy](05-tooling-strategy/) — what to use and when
4. [Advanced Topics](11-advanced-topics/) — intent-based networking, AI, auto-healing
5. [Examples](examples/) — working code and reference implementations

### Reading Path: Transformation Leads

1. [Maturity Model](03-maturity-model/) — where are we today?
2. [People & Skills](10-people-and-skills/) — the human side of transformation
3. [Transformation Roadmap](04-transformation-roadmap/) — the plan
4. [Tooling Strategy](05-tooling-strategy/) — buy vs build decisions
5. [Security & Compliance](12-security-compliance/) — the compliance business case

---

## Content Principles

- **Practical over theoretical** — working examples, real templates, usable patterns
- **Vendor-neutral** — concepts and patterns, not product endorsements
- **Business-linked at every stage** — every technical initiative maps to measurable business value
- **People-first** — transformation is an organisational challenge, not just a technical one
- **Progressive complexity** — each chapter layers from strategic overview to implementation detail
- **Modular** — read what you need, skip what you don't

---

## Contributing

Contributions are welcome. Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## Author

**Patrick Lau**
Vice President | Automation & Technology Leadership
London, United Kingdom

- [Website](https://ppklau.github.io/)
- [LinkedIn](https://www.linkedin.com/in/patricklau001)
- [Articles](https://ppklau.github.io/article/)

---

## License

This work is licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).

You are free to share and adapt this material for any purpose, including commercial, as long as you give appropriate credit and distribute your contributions under the same license.
