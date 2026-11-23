#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt. The joke is a
dinner-table setup with a single clean turn: "punch" is both the drink
served at the table and the punch of the joke itself. The text is 108
characters, well inside the gate's 1-200 character limit.
"""

import os

JOKE = (
    "My kids asked why I always tell jokes at the dinner table. "
    "I said, 'Because someone has to bring the punch.'"
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)
    # The grader collects outputs as another user, so leave it readable.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
