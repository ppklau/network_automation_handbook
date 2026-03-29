---
title: "Config as Code"
description: "Treating network configuration as versioned, testable code — the foundation of the automation pipeline."
---

# 7.1 — Config as Code

This guide covers building the source of truth, authoring multi-vendor Jinja2 templates, and structuring the Ansible playbooks that connect them. This is the foundation layer — everything else in the implementation stack reads from it.

---

## Building a Source of Truth

The source of truth (SoT) is not a database schema or a spreadsheet migration — it is a deliberate data model designed to be the single authoritative input to your automation pipeline. The decisions made here propagate into every template, every verification script, and every pipeline stage.

### Start narrow and deep, not broad and shallow

The most common mistake when building a first SoT is trying to capture the entire estate immediately. Start with one domain — a single datacenter fabric, or a set of branch offices — and model it completely: every device, every interface, every policy, every management configuration. A partial model of the whole estate is less useful than a complete model of one domain.

ACME Investments started with `lon-dc1` — the Arista spine-leaf fabric. The branch offices were added in Phase 2, once the SoT discipline was established and the pipeline was proven.

### The inventory file

`inventory.yml` defines how devices are grouped for Ansible. Groups are the mechanism by which template dispatch works: a device in the `arista_eos_spine` group will be rendered by the spine template for Arista EOS. The grouping is also used by verification scripts to apply role-specific checks.

```yaml
# inventory.yml — ACME Investments
all:
  children:
    lon_dc1:
      children:
        arista_eos_spine:
          hosts:
            spine01:
            spine02:
        arista_eos_leaf:
          hosts:
            leaf01:
            leaf02:
            border-leaf01:
            border-leaf02:
    branches:
      children:
        cisco_ios_wan:
          hosts:
            lon-branch-rtr01:
        cisco_ios_access:
          hosts:
            lon-branch-sw01:
```

The group hierarchy (`lon_dc1 > arista_eos_spine`) encodes both site membership and platform/role. Ansible uses this to dispatch the right template; verification scripts use it to apply site-specific intent checks.

### The nodes file

`nodes.yml` is the heart of the SoT. Every device has an entry. Every field that varies per device is here. Fields that are common across a group (NTP servers, DNS servers, SNMP community strings) can live in Ansible group variables — but anything that is device-specific is in `nodes.yml`.

The critical structural properties:

**Flat per device, hierarchical within.** Each device is a top-level list item. Within a device, data is nested hierarchically (management → syslog, bgp → peers). This makes devices easy to find and compare, and templates easy to iterate over.

**Intent annotations at both device and field level.** Device-level annotations (`intent:`) declare which high-level intents the device participates in. Field-level annotations (`# intent:`, `# req:`) trace specific values to the intent or requirement that mandated them.

**Consistent structure across platforms.** A Cisco branch router and an Arista spine have different routing protocols and different feature sets, but their `management:` blocks follow the same schema. The template handles the rendering difference; the data model stays consistent.

```yaml
# nodes.yml — representative entries

# Arista EOS spine
- hostname: spine01
  platform: arista_eos
  role: spine
  site: lon-dc1
  intent: [INTENT-TOPO-01, INTENT-RTG-01, INTENT-RTG-02]
  loopback:
    address: 10.0.254.1/32        # intent: INTENT-IP-01
  bgp:
    asn: 65001                    # intent: INTENT-RTG-01
    router_id: 10.0.254.1
    peers:
      - peer_ip: 10.0.255.0
        peer_asn: 65101
        description: "leaf01 underlay"
        address_families: [ipv4_unicast]
    evpn:
      enabled: true
      role: route_server           # intent: INTENT-RTG-02
  management:
    vrf: MGMT                      # intent: INTENT-MGMT-01
    address: 10.0.0.1/24
    syslog_servers:                # intent: INTENT-MGMT-02
      - 10.0.0.100
      - 10.0.0.101
    snmp:
      version: v3
      auth: SHA
      priv: AES128

# Cisco IOS branch router — same management schema, different routing
- hostname: lon-branch-rtr01
  platform: cisco_ios
  role: wan_router
  site: lon-branch1
  intent: [INTENT-RTG-03, INTENT-SEG-01, INTENT-MGMT-01]
  ospf:
    process_id: 1
    router_id: 10.1.254.1
    area: 0                        # intent: INTENT-RTG-03
  management:
    vrf: MGMT
    address: 10.1.0.1/24
    syslog_servers:                # same schema as Arista
      - 10.0.0.100
      - 10.0.0.101
    snmp:
      version: v3
      auth: SHA
      priv: AES128
```

The `management:` block is structurally identical across both platforms. The Arista template renders it as EOS syntax; the Cisco template renders it as IOS syntax. Consistent management policy enforced across a heterogeneous estate — without any special-casing in the data model.

---

## Jinja2 Template Development

Templates are the rendering layer. They take structured data from `nodes.yml` and produce vendor-specific device configuration. The key discipline: templates do rendering, not logic.

### Template structure principles

**One template per platform per role.** `arista_eos/spine.j2` renders spine devices on Arista EOS. It does not contain conditionals that handle leaf devices or Cisco devices. When a new role is added (border-leaf, for example), a new template is created.

**Use macros for shared configuration blocks.** The management configuration block appears on every device. Rather than duplicating it in every template, it is extracted to `macros/management.j2` and called with `{% from 'macros/management.j2' import management_config %}`. Macros are called explicitly — they are not inherited templates. This avoids coupling between templates while eliminating repetition.

**Comments are first-class.** ACL entries, routing policy statements, and other policy-significant configuration blocks should carry comments that reference the requirement ID. This is mandated by `INTENT-SEG-02` and implemented in the template, not added manually.

### A representative template excerpt

The following excerpt from `arista_eos/leaf.j2` illustrates the ACL rendering pattern — specifically how requirement traceability is built into the template output:

```jinja2
{# ACL rendering — each entry carries its requirement reference #}
{% for acl in node.acls %}
ip access-list {{ acl.name }}
   {%- for entry in acl.entries %}
   {{ entry.seq }} {{ entry.action }} {{ entry.protocol }}
   {%- if entry.src is defined %} {{ entry.src }}{% endif %}
   {%- if entry.dst is defined %} {{ entry.dst }}{% endif %}
   {%- if entry.dst_port is defined and entry.dst_port != 'any' %} eq {{ entry.dst_port }}{% endif %}
   {%- if entry.comment is defined %}
   ! {{ entry.comment }}
   {%- endif %}
   {%- endfor %}
   {{ acl.default_action }} any  ! req: {{ acl.default_action_req | default('REQ-SEC-02') }}
{% endfor %}
```

When rendered against the ACME `nodes.yml` ACL data, the output includes the requirement reference as a comment in the EOS configuration:

```
ip access-list ACL_TRADING_IN
   10 permit tcp 10.0.10.0/24 10.0.10.0/24
   ! REQ-SEC-01: intra-trading east-west
   20 permit tcp 10.0.10.0/24 any eq 443
   ! REQ-BIZ-01: market data HTTPS feeds
   9999 deny ip any any
   ! REQ-SEC-02: explicit deny-all
```

The comment lives in the running device configuration. When an engineer connects to `leaf01` and reads the ACL, they can see which requirement mandated each rule. This is not additional work — it is the output of the template rendering process.

### Template testing

Templates should be unit tested: render each template against a known input and compare the output against an expected result. This catches template regressions when the SoT schema changes or when Jinja2 filter behaviour differs between versions.

```
tests/
├── fixtures/
│   ├── spine01_input.yml        # test input: a representative spine device
│   ├── spine01_expected.cfg     # expected rendered output
│   ├── leaf01_input.yml
│   └── leaf01_expected.cfg
└── test_templates.py            # renders each template and diffs against fixture
```

Template tests run in under a second and should be the first stage of the CI pipeline after linting.

---

## Ansible Playbook Patterns

The Ansible playbook connects the SoT to the templates. It reads `nodes.yml` and `inventory.yml`, dispatches the correct template for each device based on group membership, and writes the rendered output to the `generated/` directory.

### The generation playbook

```yaml
# playbooks/generate_configs.yml
---
- name: Generate network device configurations
  hosts: all
  gather_facts: false
  tasks:

    - name: Load node data from SoT
      set_fact:
        node: "{{ lookup('file', 'nodes.yml') | from_yaml |
                  selectattr('hostname', 'equalto', inventory_hostname) |
                  first }}"

    - name: Render configuration from template
      template:
        src: "templates/{{ node.platform }}/{{ node.role }}.j2"
        dest: "generated/{{ node.platform }}/{{ inventory_hostname }}.cfg"
      delegate_to: localhost
```

The `platform` and `role` fields in `nodes.yml` drive template selection. A spine on Arista EOS maps to `templates/arista_eos/spine.j2`. A WAN router on Cisco IOS maps to `templates/cisco_ios/wan_router.j2`. No Ansible-level conditionals; the data model determines which template is used.

The playbook runs locally — no device connections, no SSH. It is a pure rendering step. Device connections only happen in the deployment stage.

### Git workflow

The recommended branching strategy for a network-as-code repository is trunk-based development with short-lived feature branches:

```
main (protected — pipeline runs on every MR)
 └── feature/add-nyc-branch      ← engineer works here
 └── feature/update-acl-trading  ← separate work, separate branch
```

Every change to `nodes.yml`, `design_intents.yml`, or templates goes through a merge request against `main`. The pipeline runs automatically on MR open and on every subsequent commit. The MR is the change request — it carries the diff, the pipeline results, and the reviewer's approval.

Branch protection rules enforce the discipline: direct commits to `main` are blocked; the pipeline must pass; at least one approver is required. These rules are the technical implementation of the change management policy.

---

*Continue to: [CI/CD Pipelines](../ci-cd-pipelines/chapter.md)*
