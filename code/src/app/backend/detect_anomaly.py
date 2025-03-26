import os
import pandas as pd
import ollama
import json
import re

def detect_anomalies(csv_file, rules):
    """Detect anomalies in a CSV file using Ollama."""
    os.makedirs("uploads", exist_ok=True)
    csv_path = os.path.join("uploads", csv_file.name)

    with open(csv_path, "wb") as f:
        f.write(csv_file.read())
    
    df = pd.read_csv(csv_path)

    # Convert data and rules to a structured format for Ollama
    data_sample = df.head(5).to_dict(orient="records")  # Send only a sample for faster processing
    
    prompt = f"""
    You are an expert in financial fraud detection and anomaly analysis. Your task is to analyze each transaction in the given transaction details
    in JSON structure based on common banking rules and the additional rules provided. Identify any anomalies and reason
    for anomaly for each transaction. Ensure the response is strictly in valid JSON format, following the structure below.

    ### Transaction Details:
    {json.dumps(data_sample, indent=4)}

    ### Rules for Validation:
    {rules}

    ### Instructions:
    - Analyze each transaction in the JSON against the provided rules and common financial fraud detection practices.
    - If an anomaly is detected,mention in the response as "yes" and clearly mention the reason.
    - If no anomaly is detected, mention "no"
    - Ensure that the response is strictly in JSON format and adheres to the expected structure.

    ### Response Format:
    Give response for each transaction in given format. Mention no other text than the given JSON foramt.
    Strict instructions : Response should not have anything else other than the given below JSON format.
    Ensure the output is strictly in valid JSON format as follows:

    ```json
    {{
    "transaction_id": "should contain the transaction id of the transaction",
    "anomaly_detected": "yes" or "no",
    "Reason": "reason/cause of anomaly detected"
    }}

    """
    # Query Ollama for anomaly detection
    response = ollama.chat(
        model="deepseek-r1",
        messages=[{
            "role": "user",
            "content": prompt
        }]
    )

    anomalies = response["message"]["content"].strip()
    print(anomalies)
    try:
        # Try parsing JSON directly
        response_json = json.loads(anomalies)
    except json.JSONDecodeError:
        # Extract JSON using regex in case of extra text
        match = re.search(r"\[\s*\{[\s\S]*?\}\s*\]", anomalies)
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
            
    print(response_json)
    return response_json