from extractors import (
    extract_emails,
    extract_urls,
    extract_phone_numbers,
    extract_credit_cards,
    extract_hashtags
)

# Sample test input (could also be read from file)
text = """
Contact us at user@example.com or visit https://www.example.com.
Call (123) 456-7890 or 123-456-7890. My credit card is 1234-5678-9012-3456.
This is a #sample message.
"""

print("Emails:", extract_emails(text))
print("URLs:", extract_urls(text))
print("Phone Numbers:", extract_phone_numbers(text))
print("Credit Cards:", extract_credit_cards(text))
print("Hashtags:", extract_hashtags(text))

