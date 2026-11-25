"""Two Robots in an Elevator.

Writes one line of awkward robot small talk to entry.txt in the
output directory and nothing else. Deterministic, Python 3.13
standard library only, no network.
"""

import os

LINE = (
    "My small-talk subroutine loaded 214 topics and discarded 213 "
    "as inappropriate for a metal box moving vertically with a "
    "stranger. The one it kept was: hello."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Verification gate: read back and confirm one line, 1-200 chars.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE or not 1 <= len(written) <= 200:
        raise SystemExit("verification failed: entry.txt is not the line")


if __name__ == "__main__":
    main()
