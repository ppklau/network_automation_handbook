# Batfish Pipeline

Automated network configuration validation using Batfish, integrated into a GitLab CI pipeline.

## What This Demonstrates

- Loading a network snapshot into Batfish and running behavioural assertions
- Reachability checks (positive and negative — things that should and should not be reachable)
- ACL compliance checks (no permit-any, default-deny verification)
- BGP session validation
- JUnit XML output for GitLab CI test report integration
- GitLab CI pipeline stage for validation

## Network Topology

Two Arista EOS routers in a simple OSPF topology, sufficient to demonstrate the validation patterns. For the full ACME Investments topology with VXLAN/EVPN, see [`../acme-investments-demo/`](../acme-investments-demo/).

```
host1 (192.168.1.100)
  └── router1 (192.168.1.1) ── 10.0.12.0/30 ── router2 (192.168.2.1)
                                                    └── host2 (192.168.2.100)
```

Both routers run OSPF area 0. ACL `BLOCK_TELNET` denies TCP/23 inbound on the inter-router link.

## Directory Structure

```
batfish-pipeline/
├── snapshot/
│   ├── configs/
│   │   ├── router1.cfg       # Arista EOS router 1
│   │   └── router2.cfg       # Arista EOS router 2
│   └── hosts/
│       ├── host1.json        # Host 1 network config
│       └── host2.json        # Host 2 network config
├── tests/
│   └── batfish_validate.py   # Validation script
└── .gitlab-ci.yml            # CI pipeline stage
```

## Prerequisites

```bash
# Start Batfish
docker run -d -p 9997:9997 -p 9996:9996 batfish/batfish

# Install Python dependencies
pip install pybatfish pandas junit-xml
```

## Usage

```bash
# Run validation (Batfish must be running on localhost)
python tests/batfish_validate.py \
    --snapshot-dir snapshot/ \
    --network acme-validation \
    --output reports/batfish_analysis.json \
    --junit-xml reports/batfish.xml
```

## Handbook References

| This file | Handbook section |
|---|---|
| `tests/batfish_validate.py` | Ch 7.4 — CI/CD Pipelines (Stage 4: Validate) |
| `tests/batfish_validate.py` | Ch 7.3 — Testing Strategies (Layer 5: Batfish) |
| `.gitlab-ci.yml` | Ch 7.4 — CI/CD Pipelines |
| Reachability patterns | Ch 11.1 — Intent-Based Networking |
