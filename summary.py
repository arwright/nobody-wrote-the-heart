#!/usr/bin/env python3
"""Count the catalog so the README's numbers can be regenerated instead of trusted.

Usage: python3 summary.py [catalog.csv]
"""
import csv
import sys
from collections import Counter

path = sys.argv[1] if len(sys.argv) > 1 else "catalog.csv"
with open(path, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

def first_word(s):
    s = s.strip()
    for label in ("Yes", "Partly", "No", "N/A"):
        if s.startswith(label):
            return label
    return s or "(blank)"

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

print("\nVerified")
for k, v in Counter(r["Verified"].split("—")[0].strip() or "(blank)" for r in rows).most_common():
    print(f"  {v:3}  {k}")

print("\nAuthor")
for k, v in Counter(r["Author"].strip() or "(blank)" for r in rows).most_common():
    print(f"  {v:3}  {k}")
