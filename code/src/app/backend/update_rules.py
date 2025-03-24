import os
import pandas as pd
import json

RULES_FILE = "rules.json"
def save_rules(rules):
    """Save rules to a JSON file."""
    with open(RULES_FILE, "w") as f:
        json.dump(rules, f, indent=4)

def load_rules():
    """Load rules from a JSON file."""
    if os.path.exists(RULES_FILE):
        with open(RULES_FILE, "r") as f:
            return json.load(f)
    return {}

def update_rules(new_rule):
    """Update rules dynamically and save them to the file."""
    rules = load_rules()
    rule_key = f"rule_{len(rules) + 1}"
    rules[rule_key] = new_rule
    save_rules(rules)
    return rules