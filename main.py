#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — make.fun entry.

Writes one fortune-cookie line for a software engineer to /output/entry.txt.

The fortune
-----------
"A senior engineer will call your code 'interesting' today. Update your resume."

Why this line: it is a real fortune-cookie prediction ("will ... today"),
it is aimed squarely at a software engineer (code review, the loaded word
"interesting"), the joke lands on the first read, and the funniest word —
"resume" — sits at the very end. It is not a recycled mug joke: no Friday
deploy, no "works on my machine", no "have you tried turning it off and
on again".
"""

import os

FORTUNE = "A senior engineer will call your code 'interesting' today. Update your resume."

MAX_CHARS = 120


def main() -> None:
    if not 1 <= len(FORTUNE) <= MAX_CHARS:
        raise ValueError(f"fortune is {len(FORTUNE)} chars, must be 1-{MAX_CHARS}")
    if FORTUNE != FORTUNE.strip() or "\n" in FORTUNE:
        raise ValueError("fortune must be a single line with no surrounding whitespace")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    print(FORTUNE)
    print(f"({len(FORTUNE)} chars, limit {MAX_CHARS})")


if __name__ == "__main__":
    main()
