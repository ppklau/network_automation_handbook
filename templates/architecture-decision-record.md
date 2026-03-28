# Architecture Decision Record (ADR)

**ADR number:** ADR-[NNN]
**Title:** [Short, specific title — e.g., "Source of Truth: YAML files in Git vs NetBox"]
**Date:** [YYYY-MM-DD]
**Status:** [Proposed / Accepted / Superseded / Deprecated]
**Supersedes:** [ADR-NNN, if applicable]
**Superseded by:** [ADR-NNN, if applicable]

---

## Context

*Describe the situation and the problem being solved. What is the question this decision answers? What constraints, requirements, or events made this decision necessary? Write for someone who was not in the room.*

---

## Decision

*State the decision clearly and directly. What was decided? This should be a single, unambiguous statement.*

**We will [decision].**

---

## Rationale

*Explain why this decision was made. What factors were most important? What evidence, analysis, or experience informed the choice? Be specific.*

---

## Alternatives Considered

*List the alternatives that were evaluated and why they were not chosen. This is important — it prevents the same debate from resurfacing.*

| Alternative | Why Not Chosen |
|---|---|
| | |
| | |
| | |

---

## Trade-offs Accepted

*What are the downsides, costs, or risks of this decision? What are we giving up by not choosing one of the alternatives? Being explicit about trade-offs demonstrates that the decision was made thoughtfully, not naively.*

---

## Implications

*What changes as a result of this decision? What other decisions or work does this enable, require, or constrain?*

---

## Review Triggers

*Under what circumstances should this decision be revisited? (e.g., if team size exceeds X, if a specific technology becomes available, if requirements change in a defined way)*

---

## Participants

| Name | Role |
|---|---|
| | |
| | |

---

## Example ADRs for Network Transformation Programmes

The following are examples of decisions that typically warrant an ADR. Use them as prompts when planning your programme.

| Decision Area | Example Question |
|---|---|
| Source of truth | Structured YAML in Git vs dedicated DCIM/IPAM platform vs hybrid? |
| Version control branching | Trunk-based development vs GitFlow vs environment branches? |
| Pipeline architecture | Single pipeline for all change types vs per-domain pipelines? |
| Policy enforcement | Pre-commit hooks vs CI gate vs runtime enforcement? |
| Self-service interface | API-first vs portal vs ITSM integration vs all three? |
| Approval model | Automated approval for low-risk changes vs human approval always required? |
| Rollback strategy | Automatic rollback on failure vs manual operator decision? |
| Intent abstraction level | Service-level intent vs device-level intent vs hybrid? |
| Telemetry platform | Streaming telemetry vs SNMP polling vs hybrid? |
| Secrets management | Vault-based secrets vs environment variables vs platform-native? |
