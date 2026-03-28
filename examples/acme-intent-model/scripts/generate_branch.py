#!/usr/bin/env python3
"""
generate_branch.py — ACME Investments one-touch branch site generator

Generates a fully intent-compliant SoT entry for a new branch site.
The engineer supplies only site-specific parameters; all design decisions
are derived from design_intents.yml.

Usage:
    python generate_branch.py \\
        --site-id    nyc-branch1 \\
        --location   "New York, US" \\
        --prefix     10.2.0.0/16 \\
        --router-ip  10.2.0.1/24 \\
        --router-lo  10.2.254.1/32 \\
        --switch-ip  10.2.0.11/24 \\
        --switch-lo  10.2.254.11/32 \\
        --nodes      inventory/nodes.yml \\
        --intents    design_intents.yml \\
        [--dry-run] [--verify]

Guardrails enforced:
    - Prefix overlap detection against all existing site prefixes
    - Duplicate site-id detection
    - Site-id naming convention validation
    - Intent verification before writing nodes.yml

Exit codes:
    0 — success (or dry-run completed)
    1 — guardrail failure or intent verification failure
"""

import argparse
import ipaddress
import re
import sys
from pathlib import Path
from typing import Optional

import yaml

# Import the verification suite
sys.path.insert(0, str(Path(__file__).parent.parent / "tests"))
from verify_intents import run_all_checks


# ── Guardrails ───────────────────────────────────────────────────────────────

class GuardrailError(Exception):
    pass


def validate_site_id(site_id: str) -> None:
    """Site ID must match naming convention: [a-z]{3}-branch[0-9]+"""
    pattern = r"^[a-z]{3}-branch[0-9]+$"
    if not re.match(pattern, site_id):
        raise GuardrailError(
            f"Site ID '{site_id}' does not match naming convention "
            f"'[a-z]{{3}}-branch[0-9]+' (e.g. nyc-branch1, lon-branch2)"
        )


def check_duplicate_site(site_id: str, existing_nodes: list) -> None:
    """Fail if site ID already exists in nodes.yml."""
    existing_sites = {node.get("site") for node in existing_nodes}
    if site_id in existing_sites:
        raise GuardrailError(
            f"Site '{site_id}' already exists in nodes.yml. "
            f"Use a different site ID or check whether you meant to update an existing site."
        )


def extract_prefixes(node: dict) -> list:
    """Extract all IP prefixes defined on a node."""
    prefixes = []
    lo = node.get("loopback", {})
    if lo.get("address"):
        try:
            prefixes.append(ipaddress.ip_network(lo["address"], strict=False))
        except ValueError:
            pass
    for iface in node.get("interfaces", []):
        ip = iface.get("ip")
        if ip and ip != "dhcp":
            try:
                prefixes.append(ipaddress.ip_network(ip, strict=False))
            except ValueError:
                pass
    mgmt_addr = node.get("management", {}).get("address")
    if mgmt_addr:
        try:
            prefixes.append(ipaddress.ip_network(mgmt_addr, strict=False))
        except ValueError:
            pass
    return prefixes


def check_prefix_overlap(new_prefix: str, existing_nodes: list) -> None:
    """No two sites may use overlapping IP prefixes."""
    try:
        new_net = ipaddress.ip_network(new_prefix, strict=False)
    except ValueError as e:
        raise GuardrailError(f"Invalid prefix '{new_prefix}': {e}")

    for node in existing_nodes:
        for existing_net in extract_prefixes(node):
            if new_net.overlaps(existing_net):
                raise GuardrailError(
                    f"Prefix {new_prefix} overlaps with {existing_net} "
                    f"on {node['hostname']} (site: {node.get('site', '?')}). "
                    f"Choose a non-overlapping prefix."
                )


def validate_addresses_within_prefix(
    site_prefix: str,
    router_ip: str,
    router_lo: str,
    switch_ip: str,
    switch_lo: str,
) -> None:
    """All provided addresses must fall within the site prefix."""
    site_net = ipaddress.ip_network(site_prefix, strict=False)
    addresses = {
        "router_ip": router_ip,
        "router_lo": router_lo,
        "switch_ip": switch_ip,
        "switch_lo": switch_lo,
    }
    for name, addr in addresses.items():
        host_addr = ipaddress.ip_interface(addr).ip
        if host_addr not in site_net:
            raise GuardrailError(
                f"{name} {addr} does not fall within site prefix {site_prefix}"
            )


# ── Node generation ──────────────────────────────────────────────────────────

# Values derived from design_intents.yml — not supplied by the engineer
SYSLOG_SERVERS = ["10.0.0.100", "10.0.0.101"]  # INTENT-MGMT-02
SNMP_CONFIG = {"version": "v3", "auth": "SHA", "priv": "AES128"}  # INTENT-MGMT-02
OSPF_AREA = 0                                    # INTENT-RTG-03
MGMT_VRF = "MGMT"                                # INTENT-MGMT-01
CORPORATE_VLAN = 20                              # INTENT-SEG-01


def build_branch_nodes(
    site_id: str,
    location: str,
    prefix: str,
    router_ip: str,
    router_lo: str,
    switch_ip: str,
    switch_lo: str,
) -> list:
    """
    Build the SoT entries for a new branch site.
    All design decisions are derived from the intent model.
    The engineer supplies only site-specific parameters.
    """
    site_prefix_net = ipaddress.ip_network(prefix, strict=False)
    router_hostname = f"{site_id}-rtr01"
    switch_hostname = f"{site_id}-sw01"

    wan_router = {
        "hostname": router_hostname,
        "platform": "cisco_ios",
        "role": "wan_router",
        "site": site_id,
        "location": location,
        "intent": [
            "INTENT-RTG-03",    # OSPF area 0
            "INTENT-SEG-01",    # VRF segmentation
            "INTENT-MGMT-01",   # MGMT VRF
            "INTENT-MGMT-02",   # Dual syslog, SNMPv3
            "INTENT-IP-01",     # Zone-based IP allocation
        ],
        "loopback": {
            "address": router_lo,
        },
        "ospf": {
            "process_id": 1,
            "router_id": router_lo.split("/")[0],
            "area": OSPF_AREA,          # INTENT-RTG-03
            "default_route": "inject",
            "authentication": "md5",
        },
        "interfaces": [
            {
                "name": "GigabitEthernet0/0",
                "description": "WAN uplink primary",
                "ip": "dhcp",
                "zone": "wan",
            },
            {
                "name": "GigabitEthernet0/1",
                "description": "WAN uplink secondary",
                "ip": "dhcp",
                "zone": "wan",
            },
            {
                "name": "GigabitEthernet0/2",
                "description": f"LAN to {switch_hostname}",
                "ip": router_ip,
                "zone": "corporate",
            },
        ],
        "acls": [                        # INTENT-SEG-02
            {
                "name": "ACL_WAN_IN",
                "default_action": "deny",  # REQ-SEC-02
                "entries": [
                    {
                        "seq": 10,
                        "action": "deny",
                        "protocol": "ip",
                        "src": "10.0.0.0/8",
                        "dst": "any",
                        "comment": "REQ-SEC-03: block RFC1918 from WAN",
                    },
                    {
                        "seq": 20,
                        "action": "permit",
                        "protocol": "tcp",
                        "src": "any",
                        "dst": "any",
                        "dst_port": "established",
                        "comment": "REQ-NET-05: permit established return traffic",
                    },
                    {
                        "seq": 9999,
                        "action": "deny",
                        "protocol": "ip",
                        "src": "any",
                        "dst": "any",
                        "comment": "REQ-SEC-02: explicit deny-all",
                    },
                ],
            },
        ],
        "management": {                  # INTENT-MGMT-01
            "vrf": MGMT_VRF,
            "address": router_ip,
            "ssh_source_interface": "Loopback0",
            "ssh_vrf": MGMT_VRF,
            "syslog_servers": SYSLOG_SERVERS,   # INTENT-MGMT-02
            "snmp": SNMP_CONFIG,
        },
    }

    access_switch = {
        "hostname": switch_hostname,
        "platform": "cisco_ios",
        "role": "access_switch",
        "site": site_id,
        "location": location,
        "intent": [
            "INTENT-SEG-01",
            "INTENT-MGMT-01",
            "INTENT-MGMT-02",
            "INTENT-IP-01",
        ],
        "loopback": {
            "address": switch_lo,
        },
        "ospf": {
            "process_id": 1,
            "router_id": switch_lo.split("/")[0],
            "area": OSPF_AREA,
            "passive_interfaces": ["default"],
            "active_interfaces": ["Vlan1"],
        },
        "vlans": [
            {"id": CORPORATE_VLAN, "name": "CORPORATE"},
            {"id": 99, "name": "MGMT"},
        ],
        "interfaces": [
            {
                "name": "Vlan1",
                "description": "Uplink SVI to router",
                "ip": switch_ip,
            },
            {
                "name": "GigabitEthernet0/1",
                "description": f"Uplink to {router_hostname}",
                "mode": "trunk",
                "allowed_vlans": [1, CORPORATE_VLAN, 99],
            },
        ],
        "management": {
            "vrf": MGMT_VRF,
            "address": switch_ip,
            "ssh_source_interface": "Loopback0",
            "ssh_vrf": MGMT_VRF,
            "syslog_servers": SYSLOG_SERVERS,
            "snmp": SNMP_CONFIG,
        },
    }

    return [wan_router, access_switch]


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Generate a new branch site entry in nodes.yml"
    )
    parser.add_argument("--site-id",    required=True, help="Site identifier, e.g. nyc-branch1")
    parser.add_argument("--location",   required=True, help="Human-readable location, e.g. 'New York, US'")
    parser.add_argument("--prefix",     required=True, help="Site IP prefix, e.g. 10.2.0.0/16")
    parser.add_argument("--router-ip",  required=True, help="Router LAN IP/mask, e.g. 10.2.0.1/24")
    parser.add_argument("--router-lo",  required=True, help="Router loopback IP/mask, e.g. 10.2.254.1/32")
    parser.add_argument("--switch-ip",  required=True, help="Switch management IP/mask, e.g. 10.2.0.11/24")
    parser.add_argument("--switch-lo",  required=True, help="Switch loopback IP/mask, e.g. 10.2.254.11/32")
    parser.add_argument("--nodes",      required=True, help="Path to nodes.yml")
    parser.add_argument("--intents",    required=True, help="Path to design_intents.yml (for verification)")
    parser.add_argument("--dry-run",    action="store_true", help="Preview without writing nodes.yml")
    parser.add_argument("--verify",     action="store_true", help="Run intent verification after generation")
    args = parser.parse_args()

    print(f"\nGenerating branch site: {args.site_id} ({args.location})")
    print(f"  Site prefix : {args.prefix}")

    # Load existing nodes
    with open(args.nodes) as f:
        existing_nodes = yaml.safe_load(f) or []

    # ── Guardrail checks ────────────────────────────────────────────────────
    try:
        validate_site_id(args.site_id)
        check_duplicate_site(args.site_id, existing_nodes)
        check_prefix_overlap(args.prefix, existing_nodes)
        validate_addresses_within_prefix(
            args.prefix, args.router_ip, args.router_lo,
            args.switch_ip, args.switch_lo
        )
    except GuardrailError as e:
        print(f"\n[ERROR] Guardrail check failed: {e}", file=sys.stderr)
        sys.exit(1)

    # ── Generate new nodes ──────────────────────────────────────────────────
    new_nodes = build_branch_nodes(
        site_id=args.site_id,
        location=args.location,
        prefix=args.prefix,
        router_ip=args.router_ip,
        router_lo=args.router_lo,
        switch_ip=args.switch_ip,
        switch_lo=args.switch_lo,
    )

    router_hostname = f"{args.site_id}-rtr01"
    switch_hostname = f"{args.site_id}-sw01"
    print(f"  WAN router  : {router_hostname}  lo={args.router_lo}")
    print(f"  Access sw   : {switch_hostname}   lo={args.switch_lo}")
    print(f"  Intents     : INTENT-RTG-03, INTENT-SEG-01,")
    print(f"                INTENT-MGMT-01, INTENT-MGMT-02, INTENT-IP-01")

    candidate_nodes = existing_nodes + new_nodes

    # ── Intent verification ─────────────────────────────────────────────────
    if args.verify or not args.dry_run:
        print("\nRunning intent verification...")
        results = run_all_checks(candidate_nodes)
        passed = len(results.passes)
        failed = len(results.failures)
        total = len(results.results)
        print(f"Results: {passed} passed, {failed} failed out of {total}")

        if results.failures:
            print("\nIntent verification failed:", file=sys.stderr)
            for failure in results.failures:
                print(f"  {failure.intent_id}: {failure.message}", file=sys.stderr)
                if failure.detail:
                    for line in failure.detail.strip().split("\n"):
                        print(f"    {line}", file=sys.stderr)
            sys.exit(1)

    # ── Write or dry-run ────────────────────────────────────────────────────
    if args.dry_run:
        print("\n[DRY RUN] Would add to nodes.yml:")
        print(yaml.dump(new_nodes, default_flow_style=False, indent=2))
        print("[DRY RUN] No changes written.")
    else:
        with open(args.nodes, "w") as f:
            yaml.dump(candidate_nodes, f, default_flow_style=False, indent=2, allow_unicode=True)
        print(f"\nWritten {len(new_nodes)} nodes to {args.nodes}")
        print(f"  Added: {router_hostname}, {switch_hostname}")


if __name__ == "__main__":
    main()
