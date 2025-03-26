import os
import pandas as pd
import json
import ollama
import re
import pdfplumber

RULES_FILE = "rules.json"

def extract_rules_from_pdf(pdf_file):
    """Extract rules from a PDF using Ollama and store them in a JSON file."""
    os.makedirs("uploads", exist_ok=True)
    pdf_path = os.path.join("uploads", pdf_file.name)

    with open(pdf_path, "wb") as f:
        f.write(pdf_file.read())

    # Extract text from PDF
    text = extract_text_from_pdf(pdf_path)
    print(text)
    # text = str(text) if text else "" 
    prompt = f"""
    Extract data profiling rules from the following document. 
    Return the response strictly as a valid JSON object with key-value pairs.

    The JSON must be formatted as follows:
    ```json
    {{
        "rule_1": "Description of rule 1",
        "rule_2": "Description of rule 2",
        "rule_3": "Description of rule 3"
    }}
    Rules:

    Only return JSON. Do not include explanations or extra text.

    Ensure the response starts and ends with curly braces.

    Document text: {text} """

    # Get rules from Ollama chat
    response = ollama.chat(model="deepseek-r1", messages=[{"role": "user", "content": prompt}])
    print(response['message']['content'])
    # Convert response to JSON format
    raw_content = response["message"]["content"].strip()

    try:
        # Try parsing JSON directly
        response_json = json.loads(raw_content)
    except json.JSONDecodeError:
        # Extract JSON using regex in case of extra text
        match = re.search(r"\{.*\}", raw_content, re.DOTALL)
        if match:
            json_text = match.group(0)
            try:
                response_json = json.loads(json_text)
            except json.JSONDecodeError:
                print("❌ Failed to parse extracted JSON")
                response_json = {}
        else:
            print("❌ No JSON found in Ollama response")
            response_json = {}

    # Print the extracted JSON
    print("Extracted JSON:", json.dumps(response_json, indent=4))

    # Save rules to a file
    save_rules(response_json)
    return response_json

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    table_df = extract_table_from_page_range(pdf_path, start_page=58, end_page=60)
    table_json = convert_table_to_json(table_df)
    return table_json

def save_rules(rules):
    """Save rules to a JSON file."""
    with open(RULES_FILE, "w") as f:
        json.dump(rules, f, indent=4)

def extract_table_from_page_range(pdf_path, start_page, end_page):
    extracted_data = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_num in range(start_page, min(end_page, len(pdf.pages)) + 1):
            table = pdf.pages[page_num - 1].extract_table()  # Extract table from specific page
            if table:
                df = pd.DataFrame(table[1:], columns=table[0])  # Convert to DataFrame
                extracted_data.append(df)

    return pd.concat(extracted_data, ignore_index=True) if extracted_data else None

# Example usage
# pdf_path = "D:/hackathon 2025/gaidp-bot-or-not/code/rules.pdf"
# table_df = extract_table_from_page_range(pdf_path, start_page=58, end_page=60)
# print(table_df)

def convert_table_to_json(table_df):
    rules_list = []
    
    for _, row in table_df.iterrows():
        rules_list.append({
            "Field Name": row["Field Name"].replace("\n", " ").strip(),     
            "Description": row["Description"].replace("\n", " ").strip(),
            "Allowable Values": row["Allowable Values"].replace("\n", " ").strip()
        })
    
    return json.dumps(rules_list, indent=2)