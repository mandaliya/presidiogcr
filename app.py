from flask import Flask, request, jsonify
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

app = Flask(__name__)

# Initialize Presidio Analyzer and Anonymizer
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

@app.route('/anonymize', methods=['POST'])
def anonymize_text():
    # Get text from the request
    data = request.json
    text = data.get('text', '')

    # Analyze the text to find PII entities
    results = analyzer.analyze(text=text, language='en')

    # Anonymize the text
    anonymized_text = anonymizer.anonymize(text=text, analyzer_results=results)

    # Return the anonymized text
    return jsonify({"anonymized_text": anonymized_text.text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)