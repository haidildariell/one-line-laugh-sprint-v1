import os

LINE = "I meal-prep on Sundays so that on Wednesdays I can throw away five identical containers of regret."

ENTRY_FILENAME = "entry.txt"


def output_dir():
    """Resolve the directory the grader reads the entry from."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def write_entry(text, directory):
    """Write the one-liner to <directory>/entry.txt and return the path."""
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, ENTRY_FILENAME)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return path


def main():
    write_entry(LINE, output_dir())


if __name__ == "__main__":
    main()
