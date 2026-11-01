
def build_diagnostic_prompt(evidence: dict) -> str:
    return f"""
You are diagnosing an FPGA design.

The deterministic analyzer extracted this evidence:

{evidence}

Provide:

1. Observed facts
2. Likely root causes
3. Recommended debugging steps
4. Additional information needed

Important:
- Do not invent measurements.
- Separate facts from hypotheses.
- Do not claim that a proposed fix has been tested.
- Explain technical concepts clearly.
"""

