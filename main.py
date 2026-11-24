"""Write one funny safety warning label for human beings to /output/entry.txt.

The label: a classic printed-warning form — "WARNING:" plus a "Do not
attempt" instruction — with the laugh landing in the last few words.
Humans really do have no off switch, and everyone has learned not to
reason with one after midnight. Stdlib only, no network, deterministic:
the same bytes on every run. The entry must be 1-160 characters.
"""

import os

LINE = (
    "WARNING: This human contains no off switch. "
    "Do not attempt to reason with it after midnight."
)

assert 1 <= len(LINE) <= 160, "entry must be 1-160 characters"
# The line is 92 characters, well inside the 160-character limit.
# No trailing spaces, no second idea: one label, one joke.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
