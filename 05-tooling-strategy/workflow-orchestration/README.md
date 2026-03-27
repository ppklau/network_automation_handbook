# Workflow Orchestration

## Purpose

In production environments, network changes rarely happen in isolation. A single change may depend on approvals from security, capacity confirmation from another team, firewall rule updates, and DNS changes. CI/CD pipelines handle technical validation; workflow orchestration handles the coordination between teams, systems, and approval processes.

## Why CI/CD Alone Is Insufficient

CI/CD pipelines are excellent at: linting, rendering, validating, testing, and deploying configuration. They operate within a single domain of control.

Production change management requires: cross-team approvals, wait-for-dependency steps, conditional branching based on external systems, human-in-the-loop checkpoints, integration with ITSM for audit trails, and parallel execution of independent workstreams.

These are orchestration problems, not pipeline problems.

## Key Orchestration Patterns

- **Approval gates** — human approval required before proceeding (change advisory board, security review)
- **Wait-for-dependency** — pause until an external condition is met (firewall rule applied, DNS propagated)
- **Conditional branching** — different paths based on change type, risk level, or environment
- **Parallel execution** — independent workstreams run concurrently, converge at a gate
- **Human-in-the-loop** — engineer confirms intermediate state before proceeding
- **Retry and escalation** — automatic retry with escalation on repeated failure

## Integration Model

```
[Engineer opens MR]
        │
        ▼
[CI/CD Pipeline: lint → validate → test]     ← technical validation
        │
        ▼
[Orchestrator: approval → dependency wait → scheduling]     ← coordination
        │
        ▼
[CI/CD Pipeline: deploy → verify → rollback if needed]     ← execution
        │
        ▼
[Orchestrator: close change ticket → notify stakeholders]   ← completion
```

The CI/CD pipeline handles what machines are good at. The orchestrator handles what requires coordination.

## Platform Options

- **Itential** — purpose-built for network automation orchestration
- **ServiceNow Flow Designer** — integrates with ITSM, broad enterprise adoption
- **StackStorm** — open-source, event-driven, extensible
- **AWX / Ansible Automation Platform** — workflow features built on Ansible
- **Custom** — rarely recommended; building a production orchestrator is a multi-year commitment

## Buy vs Build

This is almost always buy or adopt. Building a production-grade orchestrator requires: state management, retry logic, audit logging, role-based access, API integrations, and a UI for visibility. These are commodity capabilities that mature platforms already provide.

> Build integrations between your orchestrator and your tools. Do not build the orchestrator itself.

## Cross-References

- [07 — CI/CD Pipelines](../../07-implementation-guides/ci-cd-pipelines/) — the technical pipeline that orchestration coordinates
- [07 — One-Touch Deployment](../../07-implementation-guides/one-touch-deployment/) — orchestration enables safe one-touch workflows
- [08 — Operations Automation](../../08-operations-automation/) — incident response orchestration

## Status

`draft` — content to be developed
