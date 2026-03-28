# 06 — Architecture Patterns

## Purpose

Provide reference architectures and design patterns for network automation. These are reusable blueprints that organisations can adapt to their own environments.

## Audience

- **Primary:** Network Architects, Automation Architects
- **Secondary:** Senior Engineers implementing automation

## Content Outline

### Configuration as Code
- Source of Truth as the single point of edit
- Template architecture (Jinja2) for multi-vendor environments
- Generated configuration as a build artefact — not a hand-edited file
- Repository structure patterns
- Extends: [Network Configuration As Code article](https://ppklau.github.io/article/network_configuration_as_code/)

### Intent-Based Architecture
- Three-layer model: Business Requirements → Design Intents → Source of Truth
- Intent annotations in the SoT
- Traceability chain: requirement → intent → configuration
- Extends: [From Commands to Intent article series](https://ppklau.github.io/article/intent_based_networking_part1/)

### Reference Repository Structure
- Based on the ACME Investments example
- requirements.yml, design_intents.yml, nodes.yml, templates/, playbooks/, tests/
- Version control as the governance layer

### Source of Truth Schema Design
- Hierarchical data modelling for network devices
- Platform-agnostic data with platform-specific templates
- Intent annotation patterns
- Scaling considerations (YAML → database)

### Multi-Vendor Template Architecture
- One template per platform per role
- Shared data model, platform-specific rendering
- Platform heterogeneity managed at the template layer, not the data layer

## Cross-References

- [07 — Implementation Guides](../07-implementation-guides/) — how to build these patterns
- [11 — Intent-Based Networking](../11-advanced-topics/intent-based-networking/) — the full intent model
- [examples/acme-investments-demo/](../examples/acme-investments-demo/) — working example
- [examples/acme-intent-model/](../examples/acme-intent-model/) — intent schema example

## Source Articles

- [Network Configuration As Code](https://ppklau.github.io/article/network_configuration_as_code/)
- [From Commands to Intent (Part 1)](https://ppklau.github.io/article/intent_based_networking_part1/)
- Encoding Intent (Part 2)

## Status

`complete` — chapter and templates written
