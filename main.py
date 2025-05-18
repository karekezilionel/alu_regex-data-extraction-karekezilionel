from extractors import (
    extract_emails,
    extract_urls,
    extract_phone_numbers,
    extract_credit_cards,
    extract_hashtags
)

# Read input text from the file
with open('test_inputs.txt', 'r') as file:
    text = file.read()

# Run

