
import re


def analyze_fpga_log(log: str) -> dict:
    """Extract deterministic FPGA timing evidence from a log."""

    evidence = {
        "target": "FPGA",
        "issues": [],
        "warnings": [],
    }

    # Extract worst negative slack (WNS)
    wns_match = re.search(
        r"WNS\s*[:=]\s*(-?\d+(?:\.\d+)?)",
        log,
        re.IGNORECASE,
    )

    if wns_match:
        wns = float(wns_match.group(1))
        evidence["wns_ns"] = wns

        if wns < 0:
            evidence["issues"].append(
                f"Negative slack detected: {wns} ns"
            )

    # Detect timing failure messages
    if re.search(r"timing\s+not\s+met", log, re.IGNORECASE):
        evidence["issues"].append("Timing requirements were not met")

    # Detect unconstrained paths
    if re.search(r"unconstrained\s+path", log, re.IGNORECASE):
        evidence["warnings"].append("Unconstrained path detected")

    return evidence
