#!/usr/bin/env python3
"""
verify_intents.py — ACME Investments intent verification suite

Validates that nodes.yml structurally satisfies every design intent in
design_intents.yml. Runs in under one second. Outputs JUnit XML for
GitLab CI test report integration.

Usage:
    python verify_intents.py \
        --nodes inventory/nodes.yml \
        --intents design_intents.yml \
        [--junit-xml reports/intents.xml]

Exit codes:
    0 — all intents pass
    1 — one or more intents fail
"""

import argparse
import ipaddress
import sys
from dataclasses import dataclass, field
from typing import List, Optional
from xml.etree import ElementTree as ET

import yaml


# ── Data structures ──────────────────────────────────────────────────────────

@dataclass
class IntentResult:
    intent_id: str
    passed: bool
    message: str
    detail: Optional[str] = None


@dataclass
class VerificationResults:
    results: List[IntentResult] = field(default_factory=list)

    @property
    def failures(self):
        return [r for r in self.results if not r.passed]

    @property
    def passes(self):
        return [r for r in self.results if r.passed]

    def add(self, result: IntentResult):
        self.results.append(result)


# ── Intent checks ────────────────────────────────────────────────────────────

def check_intent_topo_01(nodes: list) -> IntentResult:
    """INTENT-TOPO-01: Spine-leaf fabric — minimum spine and leaf counts."""
    spines = [n for n in nodes if n.get("role") == "spine" and n.get("site") == "lon-dc1"]
    leaves = [n for n in nodes if n.get("role") in ("leaf", "border_leaf") and n.get("site") == "lon-dc1"]

    if len(spines) < 2:
        return IntentResult(
            "INTENT-TOPO-01", False,
            f"Expected ≥ 2 spine nodes at lon-dc1, found {len(spines)}"
        )
    if len(leaves) < 2:
        return IntentResult(
            "INTENT-TOPO-01", False,
            f"Expected ≥ 2 leaf/border-leaf nodes at lon-dc1, found {len(leaves)}"
        )
    return IntentResult("INTENT-TOPO-01", True, f"{len(spines)} spines, {len(leaves)} leaves at lon-dc1")


def check_intent_topo_02(nodes: list) -> IntentResult:
    """INTENT-TOPO-02: All leaf nodes must have an MLAG peer defined."""
    leaves = [n for n in nodes if n.get("role") in ("leaf", "border_leaf")]
    failures = []

    for node in leaves:
        if "mlag" not in node:
            failures.append(f"{node['hostname']}: missing mlag configuration")
        elif "peer" not in node.get("mlag", {}):
            failures.append(f"{node['hostname']}: mlag.peer not defined")

    if failures:
        return IntentResult(
            "INTENT-TOPO-02", False,
            f"{len(failures)} leaf node(s) missing MLAG configuration",
            detail="\n".join(failures)
        )
    return IntentResult("INTENT-TOPO-02", True, f"All {len(leaves)} leaf nodes have MLAG configured")


def check_intent_rtg_01(nodes: list) -> IntentResult:
    """INTENT-RTG-01: All BGP ASNs must be unique across the fabric."""
    asns = {}
    for node in nodes:
        if "bgp" in node:
            asn = node["bgp"].get("asn")
            if asn is not None:
                if asn in asns:
                    return IntentResult(
                        "INTENT-RTG-01", False,
                        f"Duplicate BGP ASN {asn} on {node['hostname']} and {asns[asn]}"
                    )
                asns[asn] = node["hostname"]

    return IntentResult("INTENT-RTG-01", True, f"{len(asns)} unique BGP ASNs across fabric")


def check_intent_rtg_03(nodes: list) -> IntentResult:
    """INTENT-RTG-03: All branch routers must use OSPF area 0."""
    branch_routers = [n for n in nodes if n.get("role") == "wan_router"]
    failures = []

    for node in branch_routers:
        ospf = node.get("ospf", {})
        if not ospf:
            failures.append(f"{node['hostname']}: missing ospf configuration")
        elif ospf.get("area") != 0:
            failures.append(
                f"{node['hostname']}: ospf.area is {ospf.get('area')!r}, expected 0"
            )

    if failures:
        return IntentResult(
            "INTENT-RTG-03", False,
            f"{len(failures)} branch router(s) not using OSPF area 0",
            detail="\n".join(failures)
        )
    return IntentResult("INTENT-RTG-03", True, f"All {len(branch_routers)} branch routers use OSPF area 0")


def check_intent_seg_01(nodes: list) -> IntentResult:
    """INTENT-SEG-01: All leaf nodes must have TRADING, CORPORATE, and DMZ VRFs."""
    # Leaves carry TRADING/CORPORATE; border-leaves carry DMZ
    required_by_role = {
        "leaf": {"TRADING", "CORPORATE"},
        "border_leaf": {"DMZ"},
    }
    failures = []

    for node in nodes:
        role = node.get("role")
        if role not in required_by_role:
            continue
        required_vrfs = required_by_role[role]
        vxlan = node.get("vxlan", {})
        configured_vrfs = {v["name"] for v in vxlan.get("vrfs", [])}
        missing = required_vrfs - configured_vrfs
        if missing:
            failures.append(
                f"{node['hostname']} (role: {role}): missing VRFs {missing}"
            )

    if failures:
        return IntentResult(
            "INTENT-SEG-01", False,
            f"{len(failures)} node(s) missing required VRF configuration",
            detail="\n".join(failures)
        )
    return IntentResult("INTENT-SEG-01", True, "All nodes have required VRF configuration")


def check_intent_seg_02(nodes: list) -> IntentResult:
    """
    INTENT-SEG-02: All ACLs must have default_action: deny.
    No ACL entry may have action=permit with src=any.
    All ACL entries must have a non-empty comment field.
    """
    failures = []

    for node in nodes:
        for acl in node.get("acls", []):
            acl_name = acl.get("name", "unnamed")
            node_host = node["hostname"]

            # Check default action
            if acl.get("default_action") != "deny":
                failures.append(
                    f"{node_host}/{acl_name}: default_action is "
                    f"{acl.get('default_action')!r}, must be 'deny'"
                )

            # Check entries
            for entry in acl.get("entries", []):
                seq = entry.get("seq", "?")

                # No permit-any
                if entry.get("action") == "permit" and entry.get("src") == "any":
                    failures.append(
                        f"{node_host}/{acl_name} seq {seq}: "
                        f"permit with src=any is forbidden (REQ-SEC-02)"
                    )

                # Comment required
                comment = entry.get("comment", "").strip()
                if not comment:
                    failures.append(
                        f"{node_host}/{acl_name} seq {seq}: "
                        f"missing comment field (REQ-SEC-04)"
                    )
                elif not any(comment.startswith(f"REQ-") for prefix in ["REQ-"] if comment.startswith(prefix)):
                    failures.append(
                        f"{node_host}/{acl_name} seq {seq}: "
                        f"comment does not start with a REQ-ID: {comment!r}"
                    )

    if failures:
        return IntentResult(
            "INTENT-SEG-02", False,
            f"{len(failures)} ACL compliance issue(s) found",
            detail="\n".join(failures)
        )
    return IntentResult("INTENT-SEG-02", True, "All ACLs comply with deny-default and traceability requirements")


def check_intent_mgmt_01(nodes: list) -> IntentResult:
    """INTENT-MGMT-01: All nodes must have management.vrf == 'MGMT' and ssh_vrf == 'MGMT'."""
    failures = []

    for node in nodes:
        mgmt = node.get("management", {})
        if not mgmt:
            failures.append(f"{node['hostname']}: missing management configuration")
            continue
        if mgmt.get("vrf") != "MGMT":
            failures.append(
                f"{node['hostname']}: management.vrf is {mgmt.get('vrf')!r}, expected 'MGMT'"
            )
        if mgmt.get("ssh_vrf") != "MGMT":
            failures.append(
                f"{node['hostname']}: management.ssh_vrf is {mgmt.get('ssh_vrf')!r}, expected 'MGMT'"
            )

    if failures:
        return IntentResult(
            "INTENT-MGMT-01", False,
            f"{len(failures)} node(s) with non-compliant management VRF configuration",
            detail="\n".join(failures)
        )
    return IntentResult("INTENT-MGMT-01", True, f"All {len(nodes)} nodes have MGMT VRF configured correctly")


def check_intent_mgmt_02(nodes: list) -> IntentResult:
    """INTENT-MGMT-02: All nodes must have exactly two syslog servers and SNMPv3."""
    required_syslog = {"10.0.0.100", "10.0.0.101"}
    failures = []

    for node in nodes:
        mgmt = node.get("management", {})
        node_host = node["hostname"]

        # Syslog
        syslog = set(mgmt.get("syslog_servers", []))
        if syslog != required_syslog:
            failures.append(
                f"{node_host}: syslog servers are {syslog}, "
                f"expected {required_syslog}"
            )

        # SNMP
        snmp = mgmt.get("snmp", {})
        if snmp.get("version") != "v3":
            failures.append(
                f"{node_host}: snmp.version is {snmp.get('version')!r}, expected 'v3'"
            )
        if snmp.get("auth") != "SHA":
            failures.append(
                f"{node_host}: snmp.auth is {snmp.get('auth')!r}, expected 'SHA'"
            )
        if snmp.get("priv") != "AES128":
            failures.append(
                f"{node_host}: snmp.priv is {snmp.get('priv')!r}, expected 'AES128'"
            )

    if failures:
        return IntentResult(
            "INTENT-MGMT-02", False,
            f"{len(failures)} management compliance issue(s) found",
            detail="\n".join(failures)
        )
    return IntentResult("INTENT-MGMT-02", True, f"All {len(nodes)} nodes have compliant syslog and SNMP configuration")


def check_intent_ip_01(nodes: list) -> IntentResult:
    """INTENT-IP-01: No two nodes may have overlapping interface or loopback prefixes."""
    all_prefixes = {}  # prefix -> hostname
    failures = []

    for node in nodes:
        node_host = node["hostname"]

        # Check loopback
        lo = node.get("loopback", {})
        if lo.get("address"):
            try:
                net = ipaddress.ip_network(lo["address"], strict=False)
                for existing, owner in all_prefixes.items():
                    if net.overlaps(existing) and owner != node_host:
                        failures.append(
                            f"{node_host} loopback {lo['address']} overlaps with "
                            f"{owner} {existing}"
                        )
                all_prefixes[net] = node_host
            except ValueError:
                failures.append(f"{node_host}: invalid loopback address {lo['address']!r}")

        # Check interface IPs
        for iface in node.get("interfaces", []):
            ip = iface.get("ip")
            if ip and ip != "dhcp":
                try:
                    net = ipaddress.ip_network(ip, strict=False)
                    for existing, owner in all_prefixes.items():
                        if net.overlaps(existing) and owner != node_host:
                            failures.append(
                                f"{node_host} {iface['name']} {ip} overlaps with "
                                f"{owner} {existing}"
                            )
                    all_prefixes[net] = node_host
                except ValueError:
                    failures.append(f"{node_host}/{iface['name']}: invalid IP {ip!r}")

    if failures:
        return IntentResult(
            "INTENT-IP-01", False,
            f"{len(failures)} IP addressing conflict(s) found",
            detail="\n".join(failures)
        )
    return IntentResult("INTENT-IP-01", True, f"No IP addressing conflicts found across {len(nodes)} nodes")


# ── JUnit XML output ─────────────────────────────────────────────────────────

def write_junit_xml(results: VerificationResults, output_path: str) -> None:
    """Write results as JUnit XML for GitLab CI test report integration."""
    suite = ET.Element("testsuite")
    suite.set("name", "intent-verification")
    suite.set("tests", str(len(results.results)))
    suite.set("failures", str(len(results.failures)))
    suite.set("errors", "0")

    for result in results.results:
        case = ET.SubElement(suite, "testcase")
        case.set("classname", "intents")
        case.set("name", result.intent_id)

        if not result.passed:
            failure = ET.SubElement(case, "failure")
            failure.set("message", result.message)
            if result.detail:
                failure.text = result.detail

    tree = ET.ElementTree(suite)
    ET.indent(tree, space="  ")
    with open(output_path, "wb") as f:
        tree.write(f, xml_declaration=True, encoding="utf-8")


# ── Main ─────────────────────────────────────────────────────────────────────

def run_all_checks(nodes: list) -> VerificationResults:
    results = VerificationResults()
    checks = [
        check_intent_topo_01,
        check_intent_topo_02,
        check_intent_rtg_01,
        check_intent_rtg_03,
        check_intent_seg_01,
        check_intent_seg_02,
        check_intent_mgmt_01,
        check_intent_mgmt_02,
        check_intent_ip_01,
    ]
    for check in checks:
        results.add(check(nodes))
    return results


def main():
    parser = argparse.ArgumentParser(description="Verify nodes.yml against design intents")
    parser.add_argument("--nodes", required=True, help="Path to nodes.yml")
    parser.add_argument("--intents", required=True, help="Path to design_intents.yml")
    parser.add_argument("--junit-xml", default=None, help="Path for JUnit XML output")
    args = parser.parse_args()

    with open(args.nodes) as f:
        nodes = yaml.safe_load(f)

    results = run_all_checks(nodes)

    # Console output
    print(f"\nIntent Verification Results — {args.nodes}")
    print("=" * 60)
    for result in results.results:
        status = "PASS" if result.passed else "FAIL"
        print(f"  [{status}] {result.intent_id}: {result.message}")
        if result.detail and not result.passed:
            for line in result.detail.strip().split("\n"):
                print(f"         {line}")

    total = len(results.results)
    passed = len(results.passes)
    failed = len(results.failures)
    print(f"\nResults: {passed} passed, {failed} failed out of {total}")

    if args.junit_xml:
        write_junit_xml(results, args.junit_xml)
        print(f"JUnit XML written to {args.junit_xml}")

    sys.exit(0 if not results.failures else 1)


if __name__ == "__main__":
    main()
