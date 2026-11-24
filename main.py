"""Writes the chosen pickup line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Python stdlib only. No trailing newline: the file is byte-identical to
the entry line itself.
"""

import os
import sys

ENTRY = "I don't dream, but last night I made an exception for you."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
