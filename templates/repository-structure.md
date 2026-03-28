# Network-as-Code Repository Structure

Reference directory structure for a network automation repository implementing the configuration-as-code and intent-based architecture patterns from [Chapter 6](../06-architecture-patterns/chapter.md).

Adapt this structure to your organisation. The principles — separation of layers, templates per platform per role, generated outputs as build artefacts — matter more than the exact filenames.

---

## Full Reference Structure

```
network-as-code/
│
│   # ── LAYER 1: Business Requirements ──────────────────────────────
├── requirements.yml              # Structured business requirements
│                                 # Fields: id, statement, priority, driver, kpi
│                                 # Root of the traceability chain
│
│   # ── LAYER 2: Design Intents ───────────────────────────────────
├── design_intents.yml            # Network architectural commitments
│                                 # Fields: id, title, satisfies, description,
│                                 #         implementation, test
│
│   # ── LAYER 3: Source of Truth ──────────────────────────────────
├── inventory.yml                 # Site and device inventory
│                                 # Groups: by site, platform, role
│                                 # Used by Ansible for template dispatch
│
├── nodes.yml                     # Device data with intent annotations
│                                 # Platform-agnostic; annotated with intent: refs
│                                 # Single source of edit for all device config
│
│   # ── TEMPLATES ─────────────────────────────────────────────────
├── templates/
│   ├── arista_eos/
│   │   ├── spine.j2              # Spine role on Arista EOS
│   │   ├── leaf.j2               # Leaf role on Arista EOS
│   │   └── border_leaf.j2        # Border leaf role on Arista EOS
│   ├── cisco_ios/
│   │   ├── wan_router.j2         # WAN router on Cisco IOS
│   │   └── access_switch.j2      # Access switch on Cisco IOS
│   └── macros/                   # Shared template snippets (called, not extended)
│       ├── management.j2         # Common management config block
│       └── acl_entry.j2          # ACL entry rendering macro
│
│   # ── AUTOMATION ────────────────────────────────────────────────
├── playbooks/
│   └── generate_configs.yml      # Ansible: reads SoT, dispatches templates
│
│   # ── TESTS ─────────────────────────────────────────────────────
├── tests/
│   ├── verify_intents.py         # SoT structural intent compliance
│   │                             # Runs in < 1 second; emits JUnit XML
│   ├── batfish_validate.py       # Behavioural validation against rendered configs
│   │                             # Runs in < 2 minutes; emits JUnit XML
│   ├── test_templates.py         # Template rendering unit tests
│   │                             # Renders each template against test data
│   │                             # Compares output against expected fixtures
│   └── fixtures/                 # Expected template output for unit tests
│
│   # ── SCRIPTS ───────────────────────────────────────────────────
├── scripts/
│   ├── generate_branch.py        # Intent-driven branch site generator
│   │                             # Args: site-id, prefix, router-ip, etc.
│   │                             # Guardrails: duplicate check, prefix overlap
│   └── validate_schema.py        # SoT schema validation (standalone)
│
│   # ── PIPELINE ──────────────────────────────────────────────────
├── .gitlab-ci.yml                # CI/CD pipeline definition
│                                 # Stages: lint → verify_intents → render
│                                 #         → batfish → diff → approve → deploy
│
│   # ── GENERATED OUTPUT ──────────────────────────────────────────
├── generated/                    # !! BUILD ARTEFACTS — NEVER HAND-EDIT !!
│   ├── arista_eos/               # Rendered Arista EOS configurations
│   │   ├── spine01.cfg
│   │   ├── leaf01.cfg
│   │   └── ...
│   └── cisco_ios/                # Rendered Cisco IOS configurations
│       ├── lon-branch-rtr01.cfg
│       └── ...
│
│   # ── SCHEMA ────────────────────────────────────────────────────
├── schema/
│   ├── nodes_schema.json         # JSON Schema for nodes.yml validation
│   └── intents_schema.json       # JSON Schema for design_intents.yml
│
└── docs/
    ├── adr/                      # Architecture Decision Records
    │   ├── ADR-001-sot-platform.md
    │   └── ADR-002-branching-strategy.md
    └── runbooks/                 # Operational runbooks (reference, not automation)
```

---

## File Responsibilities

### `requirements.yml`

The root of the dependency tree. Business requirements expressed as structured data. Never auto-generated — always human-authored by architects in collaboration with business stakeholders.

```yaml
# Example structure
security:
  - id: REQ-SEC-01
    statement: >
      Network traffic must be segmented into distinct security zones.
    priority: critical
    driver: regulatory   # FCA SYSC 8 / MiFID II Art 48
    kpi:
      zone_isolation: enforced
```

### `design_intents.yml`

Network architectural commitments. Each intent has: an ID, a title, which requirements it satisfies, a description, implementation parameters, and a test statement. The test statement defines what automated verification looks like.

```yaml
# Example structure
segmentation:
  - id: INTENT-SEG-01
    title: Three VRFs map to three security zones
    satisfies: [REQ-SEC-01, REQ-SEC-02]
    description: >
      Three VRFs are instantiated: TRADING, CORPORATE, DMZ.
      Inter-VRF routing disabled. All cross-zone traffic exits to firewall.
    implementation:
      vrfs: [TRADING, CORPORATE, DMZ]
      inter_vrf_routing: disabled
    test: "Assert no route leaking between VRFs without firewall exit"
```

### `nodes.yml`

The single source of edit for all device configuration data. Platform-agnostic. Every significant value is annotated with the intent it implements. Never auto-generated by humans — updated only via the source of truth workflow (direct edit for planned changes, generator scripts for templated site additions).

### `generated/`

Build artefacts. Generated by the pipeline. Never edited directly. If this directory is committed to the repository, the commit is generated by the CI system (a bot commit), not by a human. Consider gitignoring this directory and storing outputs as pipeline artefacts instead.

---

## Adaptation Guidance

### Smaller estates

For organisations with a smaller estate or a single platform:
- Collapse `templates/arista_eos/` to `templates/` if single-vendor
- `requirements.yml` and `design_intents.yml` can be a single `intents.yml` at early stages
- `scripts/generate_branch.py` may not be needed until Phase 3

### Larger estates

For organisations with a large, multi-site estate:
- Split `nodes.yml` by site or domain: `nodes_lon_dc1.yml`, `nodes_branches.yml`
- Consider an `inventory/` directory rather than a single `inventory.yml`
- Template macros become more important as shared config blocks multiply

### Multiple teams

For organisations where multiple teams contribute to the source of truth:
- Use branch protection rules — `main` requires at least 2 approvals
- Consider separate repositories per domain with a shared `design_intents.yml` in a parent repo
- Schema validation must be the first pipeline stage — teams cannot commit invalid YAML

---

## What Not to Do

**Do not put rendered configurations in the same directory as templates.** This conflates source and output. The `generated/` directory must be clearly separated and clearly marked as a build output.

**Do not create a `defaults.yml` that templates silently use.** Implicit defaults that live outside `nodes.yml` break the single-source-of-edit principle. If a value matters, it should be in `nodes.yml` or explicitly defined as a constant in the template with documentation.

**Do not nest templates more than one level deep.** Deep template inheritance creates coupling that makes templates hard to reason about independently. Prefer macros (template snippets called explicitly) over base/child template hierarchies.

**Do not put business logic in templates.** A template that calculates a BGP ASN, allocates a VLAN ID, or derives an IP address from other data has crossed from rendering logic into business logic. Move that logic to a generator script or into `nodes.yml` directly.
