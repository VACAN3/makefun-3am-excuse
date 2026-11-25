#!/usr/bin/env python3
"""The 3 AM Excuse.

Writes the entry -- the excuse a hardware wallet gives for refusing to sign
a transaction at 3 AM -- to /output/entry.txt (creating the directory if
needed), and prints it.
"""

import os

ENTRY = "My only job is saying no to the 3 AM version of you."


def main() -> None:
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
