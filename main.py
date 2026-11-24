#!/usr/bin/env python3
"""One-line pitch entry for make.fun bounty
u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.

Writes a single sentence (at most 240 characters) to
/output/entry.txt. The sentence is meant to convince a friend
who has never coded to let an AI agent build their first app
idea on make.fun. Standard library only, no network, no input
files: everything the program writes is in this file.
"""

import os
import sys

# The pitch: one sentence, plain words, a concrete reason to
# say yes now (free to try), low risk (you keep the idea), and
# no overpromising (a working first version, not a finished app).
PITCH = (
    "Tell me your app idea over coffee and I'll have an AI agent "
    "build a working first version for you on make.fun \u2014 you keep "
    "the idea, you watch it take shape, and it costs you nothing "
    "to try."
)

MAX_CHARS = 240


def validate(text):
    """The gate accepts UTF-8 text of 1 to 240 characters."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("pitch must not be only whitespace")
    if len(stripped) > MAX_CHARS:
        raise ValueError(
            "pitch is %d characters, over the %d limit"
            % (len(stripped), MAX_CHARS)
        )
    # One sentence: a period followed by a space would start a
    # second one. The period inside the domain "make.fun" has no
    # space after it, so it does not count as a sentence break.
    if ". " in stripped:
        raise ValueError("pitch must be a single sentence")
    return stripped


def output_path():
    """The grader sets MAKEFUN_OUTPUT_DIR; default is /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main():
    text = validate(PITCH)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote %d characters to %s" % (len(text), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
