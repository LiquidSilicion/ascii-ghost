
from pathlib import Path

from ascii_ghost.analyzers.fpga import analyze_fpga_log
from ascii_ghost.ai.ollama import ask_ghost
from ascii_ghost.ai.prompts import build_diagnostic_prompt


def inspect_file(file_path: str):
    log = Path(file_path).read_text(encoding="utf-8")

    # Stage 1: Deterministic analysis
    evidence = analyze_fpga_log(log)

    print("\n[1] EXTRACTED EVIDENCE")
    print(evidence)

    # Stage 2: AI interpretation
    prompt = build_diagnostic_prompt(evidence)
    diagnosis = ask_ghost(prompt)

    print("\n[2] ASCII GHOST DIAGNOSIS")
    print(diagnosis)
