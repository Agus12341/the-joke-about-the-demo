"""Write the joke entry text to /output/entry.txt.

Single-line text entry for the make.fun bounty
"the-joke-about-the-demo-20261123-0112".
"""

import os

TEXT = (
    "Pair programming with my AI agent is great: it writes 500 lines in a "
    "minute, and I spend the next hour finding out why every one of them "
    "was almost right."
)

OUTPUT_PATH = "/output/entry.txt"


def check_text(text: str) -> None:
    """Gate: 1-280 Unicode code points, not only whitespace, one line."""
    if not 1 <= len(text) <= 280:
        raise ValueError(f"text must be 1-280 code points, got {len(text)}")
    if not text.strip():
        raise ValueError("text must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("text must be a single line")


def main() -> None:
    check_text(TEXT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
