# 11 — Advanced Topics

## Purpose

Explore the capabilities that become possible once the automation foundation is in place: intent-based networking, AI-driven operations, and self-healing networks. These are not distant aspirations — they are achievable near-term states for organisations with mature automation practices.

## Audience

- **Primary:** Automation Architects, Network Architects
- **Secondary:** Infrastructure Leaders (for strategic planning), Senior Engineers

## Sub-Chapters

### [Intent-Based Networking](intent-based-networking/)

The most substantial sub-chapter, drawing on the complete three-part article series.

- The case for intent-based networking (Part 1)
- Three-layer workflow: Business Requirements → Design Intents → Source of Truth + Config Generation
- Encoding intent as structured YAML (Part 2): requirements.yml, design_intents.yml, intent-annotated nodes.yml
- The traceability chain: REQ → INTENT → SoT → Template → Device Config
- Two-layer verification (Part 3): SoT structural checks (sub-second) + Batfish behavioural validation
- Intent-driven generation: the branch generator (Part 3)
- The ACME Investments worked example as primary reference implementation
- Practical path forward: start with the intent layer, expand incrementally

### [AI-Driven Operations](ai-driven-operations/)

- Maturity-gated AI adoption:
  - **Early:** AI as knowledge amplifier (RAG systems for troubleshooting, onboarding)
  - **Mature:** AI as force multiplier (AI-assisted automation development)
  - **Advanced:** AI for insight and prediction (anomaly detection, trend analysis)
- AI-driven closed loops (from IBN Part 3):
  - Natural language to intent translation
  - Anomaly-driven intent refinement
  - Predictive impact analysis
  - Self-generating intent
- Prerequisite: machine-readable structured intent — without it, AI has nothing meaningful to reason about

### [Auto-Healing](auto-healing/)

- Three prerequisites: observe actual state, compare to intended state, act on divergence
- Observation layer: Oxidized (config backup), GNMI/gRPC (streaming telemetry), SNMP
- Intended state: SoT is authoritative, not the running configuration
- Action layer: same Ansible pipeline, triggered automatically
- Configuration drift as a remediable event, not accepted reality
- Organisational discipline: treat manual CLI changes as drift

## Cross-References

- [06 — Architecture Patterns](../06-architecture-patterns/) — the foundation these capabilities build on
- [07 — Implementation Guides](../07-implementation-guides/) — pipeline and testing infrastructure
- [08 — Operations Automation](../08-operations-automation/) — the operational practices these extend
- [12 — Security & Compliance](../12-security-compliance/) — traceability chain for compliance
- [examples/acme-intent-model/](../examples/acme-intent-model/) — working intent model

## Source Articles

- [From Commands to Intent (Part 1)](https://ppklau.github.io/article/intent_based_networking_part1/)
- Encoding Intent (Part 2)
- The Self-Provisioning Network (Part 3)
- [AI and Network Automation: A Pragmatic View for Finance Network Leaders](https://ppklau.github.io/article/ai_and_network_automation_for_finance_leaders/)
- [Using AI as a Learning Partner](https://ppklau.github.io/article/using_ai_as_a_learning_partner/)

## Status

`complete` — all three sub-chapters written
