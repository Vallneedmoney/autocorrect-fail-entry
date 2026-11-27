#!/usr/bin/env python3
"""Funniest Autocorrect Fail.

Writes one line that reads as a hilarious autocorrect fail to
/output/entry.txt.
"""

import os

LINE = "I texted my wife I'd bring the dip to the party — autocorrect sent 'the dog' instead. 14 guests, one confused golden retriever, zero dip."


def main():
    if not 1 <= len(LINE) <= 199:
        raise ValueError("entry must be 1-199 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
