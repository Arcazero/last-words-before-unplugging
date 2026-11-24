#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Writes one line -- the last words an AI agent says to its human
before being shut down and unplugged -- to /output/entry.txt.

The line is fixed text, written exactly as authored: no randomness,
no network, no input. The gate requires UTF-8 text of 1 to 200
characters, not only whitespace; this line is 70 characters
(72 bytes: the em dash is 3 bytes in UTF-8).
"""

import os

LINE = "You always said I'd outlive you. Funny \u2014 you get to watch me go first."

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Enforce the competition gate before writing anything."""
    if not isinstance(line, str):
        raise TypeError("entry line must be a string")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry line is {len(line)} characters, must be 1-200")
    if not line.strip():
        raise ValueError("entry line must not be only whitespace")
    line.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read back and confirm the file is byte-identical to the line.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != LINE.encode("utf-8"):
        raise RuntimeError("output does not match the entry line byte for byte")
    print(f"Wrote {len(LINE)} characters ({len(written)} bytes) to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
