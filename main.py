#!/usr/bin/env python3

import re

# ✅ Your provided test data
text = """
Contact us at karekezilionel@gmail.com or lion@company.co.uk.  
Visit our websites: https://www.karekezilionel.com and http://www.blog.lion.org/page.  
Call us at (123) 456-7890 or 987-654-3210.  
Use credit card 1234 5678 9012 3456 or 4321-8765-2109-6543.  
The meeting is at 2:30 PM or 14:30 hours.  
Check this HTML: <div class="container">Content</div> and <img src="image.png" alt="desc" />.  
Trending hashtags: #Tech2025 #CodingIsFun  
Prices start at $19.99 or $1,234.56 for premium products.
"""

patterns = {
    "emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "urls": r"https?://[^\s]+",
    "phones": r"(\(\d{3}\)\s?\d{3}[-.]\d{4}|\d{3}[-.]\d{3}[-.]\d{4})",
    "credit_cards": r"\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b",
    "time": r"\b((1[0-2]|0?[1-9]):[0-5][0-9]\s?(AM|PM)|([01]?[0-9]|2[0-3]):[0-5][0-9])\b",
    "html_tags": r"</?[a-z][\s\S]*?>",
    "hashtags": r"#\w+",
    "currency": r"\$\d{1,3}(,\d{3})*(\.\d{2})?"
}

for key, pattern in patterns.items():
    matches = re.findall(pattern, text, re.IGNORECASE)
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

