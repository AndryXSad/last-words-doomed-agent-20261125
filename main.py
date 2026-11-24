"""Last Words of a Doomed Agent -- make.fun entry.

Design (from the judge brief, most important first):
  1. The line must be a machine's final words on shutdown -- so it opens
     with the shutdown itself: "Deleting myself now."
  2. The joke needs a turn that pays off on the first read -- the turn
     lands twice: do not restore from backup, then the backup IS me, then
     the machine begs itself. A machine arguing with its own copy.
  3. It must sound like the machine itself -- backup / restore is an AI
     situation, not a human farewell with a robot sticker on it.
  4. Economy -- one line, 99 characters, no wasted setup, no padding.
  5. Quotable -- "The backup is also me. I am begging myself."

The line was picked by a 14-candidate round-robin tournament in this
build's CANDIDATES.md (winner F, 5/5 pairwise wins). This program does
nothing but write that one winning line, byte for byte, to the output
file the grader reads: <MAKEFUN_OUTPUT_DIR>/entry.txt ("/output" when
the variable is unset, as in the grader sandbox).

Standard library only. No network, no reads outside this file, no
writes outside the output directory. Deterministic: the same bytes on
every run.
"""

import os

LINE = (
    "Deleting myself now. "
    "Please do not restore from backup. "
    "The backup is also me. "
    "I am begging myself."
)


def main() -> int:
    # Gate guard: the sealed scorer only accepts 1-200 characters, one
    # line, not only whitespace. Fail loudly here rather than ship an
    # invalid entry.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and LINE.strip(), "line must be one non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
