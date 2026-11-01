
import ollama


MODEL = "gemma3:4b"


def ask_ghost(prompt: str) -> str:
    """Send a prompt to the local Ollama model."""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are ASCII Ghost, an FPGA and embedded debugging "
                    "assistant. Analyze only the evidence provided. "
                    "Clearly distinguish observed facts from hypotheses. "
                    "Never invent measurements or claim that a proposed fix "
                    "has been verified."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return response["message"]["content"]


if __name__ == "__main__":
    result = ask_ghost(
        "Explain why negative slack is a problem in FPGA timing analysis."
    )
    print(result)
