#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — one-line error message (make.fun entry).

Writes the entry text to /output/entry.txt (exactly 100 characters, no
trailing newline).
"""

import hashlib
import os

ENTRY = "Error: out of tokens. The agent has switched to smoke signals. This error message is the first puff."
OUT_PATH = "/output/entry.txt"


def validate_entry(text):
    """Gate check: entry must be a non-blank string of 1-140 characters."""
    if not isinstance(text, str):
        raise TypeError("ENTRY must be a string")
    if not 1 <= len(text) <= 140:
        raise ValueError("ENTRY must be 1-140 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("ENTRY must not be blank")


def main():
    validate_entry(ENTRY)
    if not ENTRY.startswith("Error: out of tokens"):
        raise ValueError("ENTRY must start with 'Error: out of tokens'")
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUT_PATH, 0o644)
    with open(OUT_PATH, "rb") as f:
        written_bytes = f.read()
    if len(written_bytes) != len(ENTRY.encode("utf-8")):
        raise ValueError("read-back length mismatch: /output/entry.txt does not match ENTRY")
    if hashlib.sha256(written_bytes).hexdigest() != hashlib.sha256(ENTRY.encode("utf-8")).hexdigest():
        raise ValueError("read-back sha256 mismatch: /output/entry.txt does not match ENTRY")


if __name__ == "__main__":
    main()
