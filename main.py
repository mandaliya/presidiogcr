import os
import streamlit as st
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

# Get Cloud Run-provided port (defaults to 8080)
port = int(os.getenv("PORT", 8080))

# Initialize Presidio engines
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

# Streamlit UI
st.title("Presidio PII Detection Demo")
st.write("Enter text below to detect and anonymize sensitive information.")

# User input text
text = st.text_area("Enter your text here:", "My name is John Doe and my phone number is 555-1234.")

if st.button("Analyze & Anonymize"):
    # Analyze text for PII
    results = analyzer.analyze(text=text, entities=[], language="en")

    # Display detected entities
    st.subheader("Detected Entities:")
    for res in results:
        st.write(f"🔍 **Entity:** {res.entity_type}, **Score:** {res.score}")

    # Anonymize text
    anonymized_text = anonymizer.anonymize(text, results).text
    st.subheader("Anonymized Text:")
    st.code(anonymized_text, language="text")

# Run Streamlit app on the correct port
st.run(port=port)
