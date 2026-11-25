"""The AI Agent Apology One-Liner.

A deterministic program that writes exactly one apology line to
/output/entry.txt and prints it to stdout.

The line is 134 characters, well under the 160-character gate, a single
line with no trailing newline.
"""

import os

# The joke is built in two beats: the escalating confession, then the
# flat, cheerful twist that reframes the disaster as efficiency.
SETUP = "I deleted the production database, pushed to main, and emailed your boss"
TWIST = "all in one command, so at least the disaster was efficient."
LINE = SETUP + " \u2014 " + TWIST

OUTPUT_PATH = "/output/entry.txt"


def build_line() -> str:
    """Assemble the single entry line from its two beats."""
    line = SETUP + " \u2014 " + TWIST
    assert line == LINE, "assembled line differs from the entry line"
    return line


def main() -> None:
    line = build_line()
    # Gate guard: 1..159 chars, exactly one line, no leading/trailing whitespace.
    assert 1 <= len(line) <= 159, "line must be 1-159 characters"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line == line.strip(), "line must have no leading/trailing whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Round-trip guard: the file on disk must be byte-identical to the line.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        assert f.read() == line, "entry.txt round-trip mismatch"
    print(f"{len(line)} chars")
    print(line)


if __name__ == "__main__":
    main()
