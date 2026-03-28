# 07 — Implementation Guides

## Purpose

The most hands-on section of the handbook. Provides detailed, step-by-step guidance for implementing the architecture patterns and tooling strategies described in earlier chapters.

## Audience

- **Primary:** Automation Engineers, Network Engineers
- **Secondary:** Automation Architects (for review and governance)

## Sub-Chapters

### [Config as Code](config-as-code/)
- Building a Source of Truth from scratch
- Jinja2 template development for multi-vendor environments
- Ansible playbook patterns for configuration generation
- Repository structure and Git workflow

### [CI/CD Pipelines](ci-cd-pipelines/)
- End-to-end pipeline design (9 stages):
  1. **Lint** — YAML validation, template syntax
  2. **Generate** — Render configs from SoT
  3. **Validate** — Batfish / offline model verification
  4. **Review** — Merge request as change control
  5. **Orchestrate** — Cross-team dependencies, approvals, scheduling
  6. **Stage** — Deploy to lab / staging
  7. **Deploy** — Push to production (replace model)
  8. **Verify** — Post-change validation
  9. **Rollback** — Automated rollback on failure
- GitLab CI and GitHub Actions examples
- Pipeline artefacts as audit trail

### [Testing Strategies](testing-strategies/)
- Testing taxonomy:
  - Syntax / lint testing
  - Unit testing (template output)
  - Model-based testing (Batfish)
  - Integration testing (multi-device)
  - Post-deployment testing (live verification)
  - Regression testing (protect existing intents)
- Two-layer verification: SoT structural checks + Batfish behavioural validation
- JUnit XML reporting for pipeline integration

### [Deployment Patterns](deployment-patterns/)
- Replace vs merge configuration models
- Canary deployments (subset first)
- Blue-green patterns for network environments
- Rollback strategies and blast radius containment
- Napalm deployment patterns

### [One-Touch Deployment](one-touch-deployment/)
- Intent-driven generation: derive all design decisions from the intent model
- The ACME branch generator as a worked example
- Guardrails: prefix overlap detection, intent verification, automated validation
- Auto-deployment patterns: event-driven provisioning, API-driven self-service
- Integration with workflow orchestration for production safety

## Cross-References

- [06 — Architecture Patterns](../06-architecture-patterns/) — the designs these guides implement
- [05 — Tooling Strategy](../05-tooling-strategy/) — tool selection for each stage
- [examples/](../examples/) — working code

## Source Articles

- [Network Configuration As Code](https://ppklau.github.io/article/network_configuration_as_code/)
- [Automated Network Testing with Batfish](https://ppklau.github.io/article/automated_testing_in_network_automation/)
- Encoding Intent (Part 2)
- The Self-Provisioning Network (Part 3)

## Status

`complete` — all five sub-chapters written
