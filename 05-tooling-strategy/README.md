# 05 — Tooling Strategy

## Purpose

Guide tooling decisions with a category-based framework rather than product recommendations. Every tool choice should be evaluated against team capability, total cost of ownership, and integration complexity.

## Audience

- **Primary:** Automation Architects, Network Architects
- **Secondary:** Engineering Managers, Transformation Leads

## Content Outline

### Principles
- Choose categories, then evaluate tools within each category
- Buy commodity capabilities; build only where it creates competitive advantage
- Every tool you adopt becomes part of your operational surface
- Integration patterns matter as much as individual tool capability

### Core Tool Categories

#### Source of Truth
- YAML-based (simple, version-controlled, good for smaller environments)
- NetBox / Nautobot (scalable, API-driven, good for larger environments)
- IPAM solutions
- When to use which; trade-offs; migration paths

#### Automation Frameworks
- Ansible (broad adoption, agentless, large ecosystem)
- Nornir (Python-native, more flexible for complex logic)
- When to use which; integration patterns

#### CI/CD Pipelines
- GitLab CI (integrated, self-hosted option)
- GitHub Actions (cloud-native, marketplace)
- Pipeline design patterns for network changes

#### Workflow Orchestration
- Why CI/CD alone is insufficient for production environments
- Cross-team dependencies, approvals, wait-for-dependency patterns
- Itential, ServiceNow Flow Designer, StackStorm
- Integration with CI/CD and ITSM
- See: [workflow-orchestration/](workflow-orchestration/)

#### Testing Frameworks
- Batfish (offline model-based validation)
- pyATS (Cisco-native, live device testing)
- Custom Python assertions
- When to use which; layered testing strategy

#### Observability Platforms
- Telemetry (GNMI/gRPC, streaming)
- Logging (syslog, centralised)
- Alerting and dashboarding
- Integration with auto-remediation

#### Security & Compliance Tools
- Policy-as-code engines
- Drift detection
- Audit trail generation

### Buy vs Build Decision Framework

| Capability | Buy | Build |
|----------|-----|------|
| Source of Truth | Often Buy/Adopt | Build if highly customised |
| Automation Framework | Usually Adopt | Extend rather than build |
| CI/CD | Buy/Adopt | Rarely build |
| Workflow Orchestration | Buy/Adopt | Rarely build — multi-year commitment |
| Observability | Buy | Integrate |
| Compliance Tooling | Buy/Adopt | Build integrations |

#### Golden Rule
> Every line of code you build becomes a product you must support.

### Total Cost of Ownership
- Licensing and subscription costs
- Operational overhead (who runs it, who upgrades it)
- Development effort for integration
- Required expertise (hiring, training)
- Lifecycle cost, not just initial build

## Cross-References

- [04 — Transformation Roadmap](../04-transformation-roadmap/) — tool adoption by phase
- [07 — Implementation Guides](../07-implementation-guides/) — how to use these tools in practice
- [10 — People & Skills](../10-people-and-skills/) — team capability alignment

## Status

`complete` — chapter, workflow orchestration sub-chapter, and templates written
