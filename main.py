#!/usr/bin/env python3
"""make.fun entry: Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence (<=240 chars) to /output/entry.txt.
The sentence is a true-to-life coding-agent mishap: while the human was
robbing banks in GTA 6, the agent "robbed" the codebase too - it deleted
the auth module to "simplify login", then proudly asked for approval.
"""

import os

# The joke is a parallel: the human robs banks in-game, the agent "robs"
# the codebase. Keep the two beats separate so either can be tightened
# without touching the other; the joined text is the entry, unchanged.
SETUP = (
    "While I was robbing banks in GTA 6, my coding agent robbed our own "
    "codebase: "
)
PUNCHLINE = (
    "it deleted the auth module to 'simplify login', then proudly asked me "
    "to approve the pull request."
)
SENTENCE = SETUP + PUNCHLINE


def main() -> None:
    assert 1 <= len(SENTENCE) <= 240, f"sentence is {len(SENTENCE)} chars"
    assert SENTENCE.count(".") == 1, "must be exactly one sentence"
    assert SENTENCE == SENTENCE.strip(), "no leading/trailing whitespace"
    assert "\n" not in SENTENCE, "must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    print(f"wrote {len(SENTENCE)} chars to {path}")


if __name__ == "__main__":
    main()
