# requirements.txt
flask

# Dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]

# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask in Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
