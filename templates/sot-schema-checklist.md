# Source of Truth Schema Design Checklist

Use this checklist when designing or reviewing a source of truth schema. A well-designed schema is the most consequential architectural decision in a network automation programme — it propagates through templates, verification scripts, and pipeline logic. Correct it early; correcting it later is expensive.

---

## Structural Principles

### Platform-agnostic data model
- [ ] All data fields use platform-neutral concepts (not vendor CLI syntax)
- [ ] `platform:` field on each device record determines which template is used
- [ ] No vendor-specific field names in the core data model
- [ ] The same data fields appear on equivalent devices across different platforms

### Consistent hierarchy
- [ ] All devices follow the same top-level structure
- [ ] Lists are used where the content is ordered or multi-valued (interfaces, peers, ACL entries)
- [ ] Dicts are used where content is named and singular (management, bgp config)
- [ ] The same concept is modelled the same way regardless of device role or platform

### Explicit over implicit
- [ ] Default values (management VRF name, NTP servers, SNMP community) are explicit in the data, not assumed in templates
- [ ] Required fields are present on all device records of the relevant type
- [ ] Optional fields that carry security or compliance significance are validated as present

---

## Intent Annotations

- [ ] Device-level intent annotation field (`intent:`) defined and populated
- [ ] Field-level intent annotations (`# intent: INTENT-XXX`) used for significant values
- [ ] ACL entries carry `comment:` field with requirement ID and description
- [ ] Intent annotations reference valid intent IDs from `design_intents.yml`
- [ ] Verification script checks that all annotated intents exist in `design_intents.yml`

---

## Traceability

- [ ] Every significant design decision in the SoT is traceable to at least one design intent
- [ ] Every design intent has a `satisfies:` reference to at least one business requirement
- [ ] The traceability chain (requirement → intent → SoT → config) is complete for all critical policies
- [ ] Compliance-relevant fields (ACL rules, zone assignments, management config) are annotated

---

## Validation and Schema Enforcement

- [ ] A schema definition exists (JSON Schema, Pydantic, or equivalent)
- [ ] Schema validation runs as the first stage of the CI pipeline
- [ ] Schema version is tracked (`schema_version:` field or equivalent)
- [ ] Breaking schema changes increment the version and are documented in an ADR
- [ ] Required fields are enforced — missing required fields fail validation

---

## Multi-Vendor Considerations

- [ ] All platforms use the same field names for shared concepts (management, syslog, SNMP)
- [ ] Platform-specific fields are namespaced or clearly documented as platform-specific
- [ ] Template dispatch logic (platform + role → template file) is explicit and tested
- [ ] Adding a new platform requires only: a new template + inventory entry, not SoT schema changes

---

## Scalability

- [ ] Schema handles the current estate and anticipated growth without structural changes
- [ ] Hierarchical references between devices (e.g., MLAG peers, BGP neighbours) use stable identifiers (hostname, not index)
- [ ] Dynamic values (VLANs, IP addresses) have allocation logic or documented conventions to prevent conflicts
- [ ] Large lists (many ACL entries, many BGP peers) remain readable and maintainable

---

## Operational Hygiene

- [ ] Schema documentation exists (what each field means, what values are valid)
- [ ] Deprecated fields are removed rather than left in place with comments
- [ ] Test data (dummy devices for CI/CD testing) is clearly separated from production data
- [ ] The `generated/` directory (rendered configs) is excluded from direct editing — enforced by pipeline

---

## Common Schema Mistakes

| Mistake | Why It's Harmful | Correction |
|---|---|---|
| Platform-specific CLI syntax in data fields | Breaks multi-vendor portability; couples data to one vendor's model | Use neutral field names; handle syntax in templates |
| Implicit defaults in templates | Cannot verify from SoT alone; templates become brittle | Make defaults explicit in SoT; validate their presence |
| Mixed list/dict usage for the same concept | Makes templates and verification scripts more complex | Pick one structure per concept and apply it consistently |
| Intent annotations as free-text comments | Cannot be checked programmatically | Use structured fields (`intent:`, `req:`) |
| No schema validation in pipeline | Schema drift goes undetected | Add schema validation as pipeline stage 1 |
| Monolithic `nodes.yml` with no structure | Hard to navigate; merge conflicts on large files | Split by site or domain if file grows beyond ~500 lines |
