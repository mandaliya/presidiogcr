from flask import Flask, request, jsonify
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
import os

app = Flask(__name__)

# Initialize Presidio engines
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

@app.route('/anonymize', methods=['POST'])
def anonymize_text():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Analyze text for PII
    results = analyzer.analyze(text=text, entities=["PERSON", "PHONE_NUMBER", "EMAIL_ADDRESS"], language='en')

    # Anonymize detected PII
    anonymized_text = anonymizer.anonymize(text=text, analyzer_results=results)

    return jsonify({"anonymized_text": anonymized_text.text})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  # Google Cloud Run requires port 8080
    app.run(host='0.0.0.0', port=port)
