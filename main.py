#!/usr/bin/env python3

import re

patterns = {
    "emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    # Improved URL pattern to match full URLs, including paths and query params
    "urls": r"https?://[^\s]+",
    # Phone numbers: includes formats like (123) 456-7890, 123-456-7890, 123.456.7890
    "phones": r"(\(\d{3}\)\s?\d{3}[-.]\d{4}|\d{3}[-.]\d{3}[-.]\d{4})",
    # Credit card: 4 groups of 4 digits separated by space or dash
    "credit_cards": r"\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b",
    # Time in 12-hour (with AM/PM) or 24-hour format
    "time": r"\b((1[0-2]|0?[1-9]):[0-5][0-9]\s?(AM|PM)|([01]?[0-9]|2[0-3]):[0-5][0-9])\b",
    "html_tags": r"</?[a-z][\s\S]*?>",
    "hashtags": r"#\w+",
    "currency": r"\$\d{1,3}(,\d{3})*(\.\d{2})?"
}

with open("test_inputs.txt", "r") as file:
    text = file.read()

for key, pattern in patterns.items():
    matches = re.findall(pattern, text, re.IGNORECASE)
    # For time, re.findall returns tuples — flatten the matches by picking the first non-empty
    if key == "time":
        flat_matches = []
        for m in matches:
            for item in m:
                if item:
                    flat_matches.append(item)
                    break
        matches = flat_matches
    print(f"\n🔎 {key.upper()}:")
    print(matches)
