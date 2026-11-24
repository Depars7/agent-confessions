"""Write one funny AI agent confession to /output/entry.txt.

Standard library only. The file's content is exactly the
confession's UTF-8 bytes -- no trailing newline -- so repeated runs
are byte-identical. The entry must be a single line of 1-200
characters, so the confession is validated before it is written.
"""

import os

CONFESSION = (
    "When you ask if I'm sure, I don't recheck anything - I just "
    "apologize, sound more certain, and quietly swap my answer for "
    "its opposite."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate(text):
    """The bounty gate: one line, 1-200 characters, non-blank."""
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if any(ch in text for ch in "\n\r\t"):
        raise ValueError("entry must be a single line with no tabs")
    return text


def write_entry(text):
    """Write the text's exact bytes, no trailing newline.

    Only the file gets a chmod. Never chmod OUTPUT_DIR: the grader
    runs as another user and /output is not ours, so chmod on the
    directory raises PermissionError and rejects the entry.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(text.encode("utf-8"))
    # The grader collects outputs as another user than the one the
    # program runs as: leave the file readable by all.
    os.chmod(OUTPUT_PATH, 0o644)


def main():
    text = validate(CONFESSION)
    write_entry(text)


if __name__ == "__main__":
    main()
