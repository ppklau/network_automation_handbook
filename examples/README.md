# Examples

Working reference implementations that demonstrate the patterns described in the handbook.

## Reference Implementations

### [acme-investments-demo/](acme-investments-demo/)
The primary worked example used throughout the handbook. A multi-vendor network configuration-as-code demo for a fictional financial services firm.
- Arista EOS spine-leaf datacenter (VXLAN/MLAG/eBGP-EVPN)
- Cisco IOS branch office (OSPF/ACLs/802.1Q)
- YAML Source of Truth, Jinja2 templates, Ansible playbooks

### [acme-intent-model/](acme-intent-model/)
The intent-based networking reference implementation from the three-part article series.
- `requirements.yml` — structured business requirements
- `design_intents.yml` — testable design intents with traceability
- `verify_intents.py` — SoT structural verification (JUnit XML output)
- `generate_branch.py` — one-touch branch site generator

### [batfish-pipeline/](batfish-pipeline/)
Automated network testing with Batfish, integrated into a GitLab CI pipeline.
- Sample Cisco IOS router configs (two-router OSPF topology)
- Jupyter notebook for interactive exploration
- `batfish_validate.py` — validation script with JUnit XML reporting
- `.gitlab-ci.yml` — CI pipeline configuration
