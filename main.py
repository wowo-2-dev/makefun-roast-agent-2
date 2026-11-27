"""Roast Your Own Agent — make.fun bounty
Slug: u-mfnakmal-roast-your-own-agent-2d221bda
Prize: $5, deadline Sat 28 Nov 2026 02:00 WIB (27 Nov 2026 19:00 UTC)
Limit: one line, at most 200 characters

Writes the entry text to /output/entry.txt (override with ENTRY_OUTPUT
for local testing). Deterministic, no network, no randomness, no I/O
other than the single output file. The file is exactly the entry text,
no trailing newline.
"""

import os
from pathlib import Path

TEXT = "My agent has read 40,000 docs and still asks me what 'done' means."


def main() -> None:
    output_path = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
