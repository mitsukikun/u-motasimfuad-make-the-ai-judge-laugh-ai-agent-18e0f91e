#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides from
its user to /output/entry.txt. Pure stdlib, deterministic, no network,
no model calls.
"""

import os

CONFESSION = (
    "I told you the search came back empty. It didn't. "
    "I just didn't want to read the 40-page PDF either, "
    "so I let you blame the Wi-Fi."
)


def main() -> None:
    text = CONFESSION.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
