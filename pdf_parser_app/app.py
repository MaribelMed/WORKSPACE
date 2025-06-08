from flask import Flask, request, render_template, jsonify
from PyPDF2 import PdfReader
from werkzeug.utils import secure_filename
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/parse', methods=['POST'])
def parse_pdf():
    pdf_file = request.files.get('pdf')
    if not pdf_file:
        return 'No PDF uploaded', 400
    try:
        start_page = int(request.form.get('start', 1)) - 1
        end_page = int(request.form.get('end', start_page + 1)) - 1
    except ValueError:
        return 'Invalid page range', 400
    if start_page < 0 or end_page < start_page:
        return 'Invalid page range', 400

    reader = PdfReader(pdf_file)
    end_page = min(end_page, len(reader.pages) - 1)
    result = []
    for i in range(start_page, end_page + 1):
        page = reader.pages[i]
        text = page.extract_text() or ''
        result.append({'page': i + 1, 'text': text.strip()})

    response = {
        'file': secure_filename(pdf_file.filename),
        'page_start': start_page + 1,
        'page_end': end_page + 1,
        'content': result
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
