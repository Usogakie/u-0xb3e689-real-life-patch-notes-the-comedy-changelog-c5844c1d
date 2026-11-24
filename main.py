"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch-note line to ${MAKEFUN_OUTPUT_DIR:-/output}/entry.txt.
The line is a single changelog entry for a bug in human biology, in the
terse register of a real release note. It is written with no trailing
newline so the file holds exactly the 138 characters of the line.
"""

import os

LINE = (
    "v2.4.1: fixed a bug where the brain replayed your most embarrassing "
    "moment from 2009 every night at 3:00 AM, on loop, with no skip button."
)


def main() -> None:
    # Self-check against the competition gate: 1 to 160 characters.
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars, gate is 1-160"
    assert LINE.strip() == LINE and "\n" not in LINE, "line must be one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
