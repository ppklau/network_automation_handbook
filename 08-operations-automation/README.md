# 08 — Operations Automation

## Purpose

Guide the automation of day-to-day network operations: monitoring, incident response, change execution, and auto-remediation. This is where automation delivers its most visible daily value.

## Audience

- **Primary:** Operations Engineers, Automation Engineers
- **Secondary:** Network Infrastructure Leaders (for operational KPIs)

## Content Outline

### Monitoring & Observability
- Telemetry collection (GNMI/gRPC, SNMP, syslog)
- Centralised logging and alerting
- Dashboard design for operational visibility
- Alert noise reduction strategies

### Incident Response Automation
- Automated diagnostics on alert trigger
- Runbook automation (structured troubleshooting workflows)
- Escalation patterns
- Integration with ITSM (ServiceNow, Jira Service Management)

### Change Execution
- Automated change windows
- Pre-change and post-change validation
- Diff-based deployment (show exactly what changes)
- Rollback automation

### Auto-Remediation
- Configuration drift detection (Oxidized, scheduled SoT comparison)
- Automated drift correction
- Telemetry-driven remediation (event → diagnosis → action)
- Risk-tiered remediation: auto-fix low-risk, alert-and-propose for high-risk

### The Feedback Loop
- Telemetry data feeding back into Source of Truth and automation decisions
- Closed-loop concept: observe → compare to intent → remediate
- This is the bridge between operations and the advanced topics (Chapter 11)

### Product Thinking for Operations
- Treating operational automation as a product with users, feedback, and iteration
- Metrics: MTTR, MTTD, incident auto-resolution rate, change failure rate
- Extends: [Why Network Automation Needs Product Thinking](https://ppklau.github.io/article/why_network_automation_needs_product_thinking/)

## Cross-References

- [05 — Tooling Strategy](../05-tooling-strategy/) — observability and orchestration tools
- [07 — Implementation Guides](../07-implementation-guides/) — pipeline and deployment patterns
- [11 — Auto-Healing](../11-advanced-topics/auto-healing/) — the advanced evolution of auto-remediation
- [13 — Dashboards](../13-dashboards/) — operations view metrics

## Source Articles

- [Why Network Automation Needs Product Thinking](https://ppklau.github.io/article/why_network_automation_needs_product_thinking/)

## Status

`draft` — content to be developed
