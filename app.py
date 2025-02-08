import streamlit as st
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

# Initialize Presidio engines
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

st.title("PII Anonymization with Presidio")
st.write("Enter text to anonymize sensitive information:")

# Text input
user_input = st.text_area("Input Text")

if st.button("Anonymize"):
    if user_input:
        # Analyze text for PII entities
        results = analyzer.analyze(text=user_input, entities=[], language='en')
        
        # Anonymize detected PII entities
        anonymized_result = anonymizer.anonymize(text=user_input, analyzer_results=results)
        
        st.subheader("Anonymized Text:")
        st.write(anonymized_result.text)
    else:
        st.write("Please enter some text to anonymize.")
