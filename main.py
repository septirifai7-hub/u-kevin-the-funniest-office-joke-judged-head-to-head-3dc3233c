"""Entry for "The Funniest Office Joke, Judged Head to Head".

The bounty asks for one joke about office life, a single line of
under two hundred characters, with the punchline last and every word
earning its place.

The line below treats the office tools as co-workers with feelings:
the meeting runs so long that even the ticketing system complains,
and the coffee machine — the one thing holding the office together —
hands in its notice. The escalation from Jira to the coffee machine
is the punchline.
"""

ENTRY = (
    "Our standup ran so long the Jira tickets filed a complaint about "
    "us, and the coffee machine handed in its resignation in the chat."
)


def get_entry():
    """Return the entry line exactly as it should be judged."""
    return ENTRY


def write_entry():
    """Write the entry to the output directory and return its path."""
    import os

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(get_entry())
    return path


def main():
    path = write_entry()
    print(f"Wrote entry to {path}")


if __name__ == "__main__":
    main()
