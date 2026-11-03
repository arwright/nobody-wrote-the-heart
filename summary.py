#!/usr/bin/env python3
"""Count the catalog so the README's numbers can be regenerated instead of trusted.

Usage: python3 summary.py [catalog.csv]
"""
import csv
import re
import sys
from collections import Counter

path = sys.argv[1] if len(sys.argv) > 1 else "catalog.csv"
with open(path, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

def first_word(s):
    """The first keyword in the cell, so "David: Yes ... Walter: No" counts as Yes."""
    m = re.search(r"\b(Yes|Partly|No|N/A)\b", s)
    return m.group(1) if m else s.strip() or "(blank)"

print(f"Works: {len(rows)}\n")

print("Explanation category")
for k, v in Counter(r["Explanation category"] for r in rows).most_common():
    print(f"  {v:3}  {k}")

print("\nWho wrote the prompt — shown?")
for k, v in Counter(first_word(r["Who wrote the prompt — shown?"]) for r in rows).most_common():
    print(f"  {v:3}  {k}")

print("\nRecognition vs. caring distinguished?")
for k, v in Counter(first_word(r["Recognition vs. caring distinguished?"]) for r in rows).most_common():
    print(f"  {v:3}  {k}")

print("\nBreaks its prompt?")
for k, v in Counter(first_word(r["Breaks its prompt?"]) for r in rows).most_common():
    print(f"  {v:3}  {k}")

print("\nVerified")
for k, v in Counter(r["Verified"].split("—")[0].strip() or "(blank)" for r in rows).most_common():
    print(f"  {v:3}  {k}")

print("\nAuthor")
for k, v in Counter(r["Author"].strip() or "(blank)" for r in rows).most_common():
    print(f"  {v:3}  {k}")
