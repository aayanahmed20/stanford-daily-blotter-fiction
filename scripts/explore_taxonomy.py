"""
Reference script for the taxonomy exploration that inspired "Lot 95."

The blotter's prose treats every incident as a one-off. This script
reproduces the actual step that surfaced the pattern: parsing each
article's HTML for location/incident mentions, then counting which
locations recur most often for a given incident type - the kind of
count that never shows up in the prose itself, only in the underlying
data.

Requires: datasets, beautifulsoup4
    pip install datasets beautifulsoup4
"""

import re
from collections import Counter

from bs4 import BeautifulSoup
from datasets import load_dataset

# Incident phrase to look for. "Burglary from a motor vehicle" and
# "vehicle burglary" are the two phrasings the blotter actually uses.
INCIDENT_PATTERN = re.compile(
    r"(burglary from a motor vehicle|vehicle burglary|burglary of a motor vehicle)",
    re.IGNORECASE,
)

# Crude location extractor: blotter items are written as
# "... was reported at <location>." or "... occurred at <location>.",
# with the location sometimes followed by a parenthetical building name.
LOCATION_PATTERN = re.compile(
    r"(?:reported at|occurred at)\s+([^.]+?)(?:\.|$)",
    re.IGNORECASE,
)


def extract_incidents(html: str):
    """Yield (location, sentence) pairs for vehicle-burglary items in one article."""
    soup = BeautifulSoup(html, "html.parser")
    for li in soup.find_all("li"):
        text = li.get_text(" ", strip=True)
        if INCIDENT_PATTERN.search(text):
            loc_match = LOCATION_PATTERN.search(text)
            location = loc_match.group(1).strip() if loc_match else "unknown"
            yield location, text


def main():
    ds = load_dataset("stanforddams/daily", "html")["train"]

    location_counts = Counter()
    examples_by_location = {}

    for row in ds:
        for location, sentence in extract_incidents(row["html"]):
            # Prefer the parenthetical lot/building name as the grouping
            # key. The street address for the same physical lot is written
            # inconsistently across articles (e.g. "Galvez Street" in one
            # week, "Galvez Court" in another) - which is itself a small
            # example of why the prose alone under-counts a repeat location.
            paren_match = re.search(r"\(([^)]+)\)", location)
            key = paren_match.group(1).strip().lower() if paren_match else location.strip().lower()
            location_counts[key] += 1
            examples_by_location.setdefault(key, sentence)

    print("Vehicle-burglary mentions by location (top 10):\n")
    for location, count in location_counts.most_common(10):
        print(f"{count:>3}  {location}")
        print(f"      e.g. \"{examples_by_location[location]}\"\n")


if __name__ == "__main__":
    main()
