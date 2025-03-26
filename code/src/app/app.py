import streamlit as st
import backend.update_rules as update_rules
import backend.extract_rules as extract_rules
import backend.detect_anomaly as anomaly
import pandas as pd

# Initialize rules in session state only once
if "rules" not in st.session_state:
    st.session_state.rules = update_rules.load_rules()

st.title("📊 AI-Powered Data Profiler & Anomaly Detector")

# Upload PDF for extracting rules
st.sidebar.header("Step 1: Extract Rules from PDF")
pdf_file = st.sidebar.file_uploader("Upload a PDF for Data Profiling", type=["pdf"])

if pdf_file and not st.session_state.get("rules_extracted", False):  # Prevent re-extraction
    with st.spinner("Extracting rules from PDF..."):
        st.session_state.rules = extract_rules.extract_rules_from_pdf(pdf_file)
        update_rules.save_rules(st.session_state.rules)  # Persist extracted rules
        st.session_state.rules_extracted = True  # Mark that rules are extracted
        st.sidebar.success("✅ Rules extracted and saved!")
        st.sidebar.json(st.session_state.rules)

# Ensure rules are loaded before moving to the next step
if not st.session_state.rules:
    st.warning("⚠️ No rules found! Please upload a PDF first.")
    st.stop()

# Upload CSV for anomaly detection
st.sidebar.header("Step 2: Detect Anomalies in CSV")
csv_file = st.sidebar.file_uploader("Upload a CSV for Anomaly Detection", type=["csv"])

if csv_file:
    with st.spinner("Analyzing data for anomalies..."):
        anomalies = anomaly.detect_anomalies(csv_file, st.session_state.rules)
        st.success("✅ Anomalies detected!")
        df = pd.DataFrame(anomalies)

        # Display in Streamlit
        st.dataframe(
            df,
            column_order=["transaction_id", "anomaly_detected", "Reason"],
            hide_index=True,
            use_container_width=True
        )

        # Optional: Add download button
        st.download_button(
            label="Download as CSV",
            data=df.to_csv(index=False).encode('utf-8'),
            file_name='anomaly_report.csv',
            mime='text/csv'
        )

# Chat-based Rule Updating
st.sidebar.header("Step 3: Add More Rules (Chat)")
new_rule = st.sidebar.text_input("Enter a new rule to add")

if st.sidebar.button("Save Rule") and new_rule:
    rule_id = f"rule_{len(st.session_state.rules) + 1}"
    st.session_state.rules[rule_id] = new_rule
    update_rules.update_rules(new_rule)  # Persist rules
    st.success("Rule added successfully!")
    st.sidebar.json(st.session_state.rules)

st.markdown("---")
st.markdown("🔍 **Upload a PDF to extract rules, then analyze CSV files for anomalies!**")