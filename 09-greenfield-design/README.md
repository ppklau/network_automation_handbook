# 09 — Greenfield Design

## Purpose

Present greenfield-inspired principles that apply whenever an organisation has a clean-slate opportunity — whether a new site, a new environment, a major refresh, or a true greenfield build. The principles are universal; the opportunity to apply them is more common than people think.

## Audience

- **Primary:** Network Architects, Automation Architects
- **Secondary:** Infrastructure Leaders evaluating new environments

## Content Outline

### Greenfield Principles for Any Environment
- API-first infrastructure
- Full automation from day 1
- Source of truth as foundation
- CI/CD pipelines from the start
- Immutable infrastructure concepts
- Intent-based design from the outset

### Acknowledging Real-World Constraints
- Even "greenfield" projects inherit constraints:
  - Existing vendor contracts and relationships
  - Compliance and regulatory requirements
  - Team skillsets and availability
  - Integration with existing environments
  - Budget and timeline pressures
- How to apply greenfield principles while navigating these realities

### One-Touch Deployment as a Greenfield Outcome
- The ACME branch generator: a single command produces a fully intent-compliant site
- Intent-driven generation derives all design decisions from the intent model
- Engineer provides only site-specific inputs; everything else follows from intent
- Guardrails make it safe: prefix overlap detection, intent verification, Batfish validation
- Extends: The Self-Provisioning Network (IBN Part 3)

### Auto-Deployment Patterns
- Event-driven provisioning (business event → network provisioning triggered)
- API-driven self-service portals
- Business value: time-to-revenue for new sites, scalability without proportional headcount

### People & Skills for Greenfield
- Intentional team design from day one
- Core skillsets: Network SME, Software Engineering, DevOps/Platform, Automation Architecture
- Team structure: Network SME(s) + Automation Engineers + Platform Engineers + Automation Architect

> Do not treat automation as an add-on — build a software-driven network organisation from day one.

### Buy vs Build in Greenfield
- Greenfield does not mean "build everything"
- Prefer buying when: capability is commodity, expertise is limited, speed is critical
- Prefer building when: competitive advantage, highly customised, strong software team

> Do not build systems you cannot operate, maintain, and evolve.

### The Software Mindset
- Software-centric architecture as competitive advantage
- Learning speed as a differentiator
- Extends: [What Anduril Teaches Us About Software Mindset](https://ppklau.github.io/article/what_anduril_teaches_us_about_software_mindset/)

## Cross-References

- [06 — Architecture Patterns](../06-architecture-patterns/) — reference architectures to implement
- [07 — One-Touch Deployment](../07-implementation-guides/one-touch-deployment/) — implementation detail
- [10 — People & Skills](../10-people-and-skills/) — team design
- [11 — Intent-Based Networking](../11-advanced-topics/intent-based-networking/) — the intent model

## Source Articles

- [What Anduril Teaches Us About Software Mindset](https://ppklau.github.io/article/what_anduril_teaches_us_about_software_mindset/)
- The Self-Provisioning Network (Part 3)

## Status

`draft` — content to be developed
