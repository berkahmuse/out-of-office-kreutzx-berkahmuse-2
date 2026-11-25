#!/usr/bin/env python3
"""The Funniest Out-of-Office — @berkahmuse-2 entry.

Writes a single line of out-of-office auto-reply to /output/entry.txt.
Deterministic: the same line, byte for byte, on every run.
"""

import os

ENTRY = (
    "I'm out of office until Monday, living my best life as a houseplant: "
    "watered weekly, spoken to rarely, thriving anyway."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY and "\r" not in ENTRY
    assert ENTRY.strip() == ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
