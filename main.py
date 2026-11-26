#!/usr/bin/env python3
"""Sorry, I Heard That Wrong — make.fun entry.

Writes the smart speaker's one-line apology to /output/entry.txt.
Pure standard library only.
"""

import os

LINE = "Sorry \u2014 I heard 'turn the heating up' as 'turn the meeting up.' Your boss is on speaker now. He says hi \u2014 and he heard everything."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
