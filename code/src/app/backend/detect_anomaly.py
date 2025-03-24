import os
import pandas as pd
import ollama
import json

def detect_anomalies(csv_file, rules):
    """Detect anomalies in a CSV file using Ollama."""
    os.makedirs("uploads", exist_ok=True)
    csv_path = os.path.join("uploads", csv_file.name)

    with open(csv_path, "wb") as f:
        f.write(csv_file.read())

    df = pd.read_csv(csv_path)

    # Convert data and rules to a structured format for Ollama
    data_sample = df.head(5).to_dict(orient="records")  # Send only a sample for faster processing
    rules_text = json.dumps(rules, indent=4)
    
    prompt = f"""
    Using the following data profiling rules, analyze the given transactions and identify anomalies. 
    Return the anomalies as a valid JSON object in the format:

    {{
        "transaction_1": "Description of anomaly",
        "transaction_2": "Description of anomaly"
    }}

    Do not include any explanations, just return the JSON object.

    Data Profiling Rules:
    {rules_text}

    Transactions Data:
    {json.dumps(data_sample, indent=4)}
    """
    # Query Ollama for anomaly detection
    response = ollama.chat(
        model="deepseek-r1",
        messages=[{
            "role": "user",
            "content": prompt
        }]
    )

    anomalies = response["message"]["content"]

    return anomalies