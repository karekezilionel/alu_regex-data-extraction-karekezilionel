# alu_regex-data-extraction-{KAREKEZILIONEL}

## Project Overview

This project uses **Regular Expressions (regex)** to extract various types of data from raw text strings. It is designed to parse and extract meaningful information such as emails, URLs, phone numbers, credit card numbers, time, HTML tags, hashtags, and currency amounts from unstructured text responses.

## Extracted Data Types

- **Email addresses:** e.g., `user@example.com`, `firstname.lastname@company.co.uk`  
- **URLs:** e.g., `https://www.example.com`, `http://blog.example.org/page`  
- **Phone numbers:** e.g., `(123) 456-7890`, `123-456-7890`  
- **Credit card numbers:** e.g., `1234 5678 9012 3456`, `1234-5678-9012-3456`  
- **Time:** both 12-hour (e.g., `2:30 PM`) and 24-hour formats (e.g., `14:30`)  
- **HTML tags:** e.g., `<div class="container">`, `<img src="image.png" alt="desc" />`  
- **Hashtags:** e.g., `#Tech2025`, `#CodingIsFun`  
- **Currency amounts:** e.g., `$19.99`, `$1,234.56`  

## Getting Started

### Prerequisites

- Python 3.6 or higher  
- Basic knowledge on how to run Python scripts from the command line

 **How to Run**

Clone the repository:

   bash
   
   git clone https://github.com/your-username/alu_regex-data-extraction-karekezilionel.git
   
   cd alu_regex-data-extraction-karekezilionel

###Run the script:

bash

python3 main.py


    **EXAMPLE OUTPUT**


![Capture](https://github.com/user-attachments/assets/57c017ce-cc5d-4dd1-aebe-2bcccc536064)


Code Structure
main.py — Main Python script containing regex patterns and extraction logic.





