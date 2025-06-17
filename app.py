from flask import Flask, render_template, request, jsonify
import os
import fitz  # PyMuPDF
import re

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def extract_details(text):
    name = text.strip().split('\n')[0]
    email = re.search(r'[\w\.-]+@[\w\.-]+', text)
    phone = re.search(r'\+?\d[\d\s-]{8,}\d', text)

    return {
        'name': name,
        'email': email.group() if email else '',
        'phone': phone.group() if phone else ''
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['resume']
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    doc = fitz.open(file_path)
    text = ''
    for page in doc:
        text += page.get_text()

    details = extract_details(text)
    return jsonify(details)

if __name__ == '__main__':
    app.run(debug=True)
