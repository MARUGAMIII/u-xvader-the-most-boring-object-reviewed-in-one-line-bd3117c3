#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line -- make.fun entry.

Writes a one-line review of a doorstop to /output/entry.txt
(or $OUTPUT_DIR/entry.txt).

Craft notes: the doorstop is the dullest everyday object I could
name -- a wedge whose whole existence is holding a door open.
The joke comes from how it really behaves: everyone kicks it out
of the way, and it ends up across the room, punished for doing
exactly the one job it has. The turn lands at the end ("its
reward is getting kicked"), and every word earns its place.
One line, plain ASCII, no em dash. After writing, the program reads
the file back and refuses to finish unless it is byte-identical to
the validated entry, so the judge never sees a different text than
the one checked here.

Python standard library only.
"""

import os

ENTRY = (
    "The doorstop has exactly one job, holding the door open, "
    "and its reward is getting kicked across the room for doing it."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry length {len(text)} out of range 1-200")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.isascii():
        raise SystemExit("entry must be plain ASCII")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and verify: the file the judge sees must be byte-identical
    # to the validated entry -- one line, no trailing newline, nothing added.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise SystemExit("entry.txt does not match validated entry")
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
