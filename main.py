#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — one-line error message (make.fun entry).

Writes the entry text to /output/entry.txt (exactly 100 characters, no
trailing newline).
"""

import os

ENTRY = "Error: out of tokens. The agent has switched to smoke signals. This error message is the first puff."
OUT_PATH = "/output/entry.txt"


def main():
    if not isinstance(ENTRY, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(ENTRY) <= 140:
        raise ValueError("entry must be 1-140 characters")
    if not ENTRY.strip():
        raise ValueError("entry must not be blank")
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUT_PATH, 0o644)
    with open(OUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("written entry does not match entry text")


if __name__ == "__main__":
    main()
