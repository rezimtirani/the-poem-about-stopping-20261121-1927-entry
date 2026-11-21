#!/usr/bin/env python3
"""Write one short poem about stopping and staying to /output/entry.txt."""

import os

POEM = (
    "I used to think stopping was losing —\n"
    "that the road only loved the ones who kept going.\n"
    "Then one evening I put my bag down,\n"
    "sat on the low wall, and stayed.\n"
    "Nothing broke. The light only softened.\n"
    "I had not quit. I had chosen."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(POEM)


if __name__ == "__main__":
    main()
