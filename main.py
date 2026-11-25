#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry program.

Writes one original funny rant about a small everyday annoyance
(the self-checkout machine) to /output/entry.txt.
No network, no dependencies, deterministic output.
"""

import os
import sys

RANT = (
    "I scanned my milk, bagged my milk, and the self-checkout still screamed "
    "'UNEXPECTED ITEM IN THE BAGGING AREA.' The unexpected item was the bag. "
    "I paid for the bag. The machine watched me pay for the bag. Now I'm "
    "standing there, hands up like a shoplifter, while a red light flashes "
    "over my head and a teenager named Kyle strolls over to press one button."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(RANT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
