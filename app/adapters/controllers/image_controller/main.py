from flask import Flask, request, render_template, flash, redirect, jsonify
import os, sys
sys.path.insert(0, os.path.abspath("../../.."))

from external.replicate.replicate_ai import ReplicateAPI
from providers.ai.image_use_case_provider import get_image_use_case
from use_cases.description_use_case import DescriptionUseCase
from werkzeug.utils import secure_filename

from dotenv import load_dotenv
load_dotenv()

import json
import requests

app = Flask(__name__)
app.secret_key =  os.getenv("FLASK_SECRET_KEY")

description_use_case = DescriptionUseCase(ReplicateAPI())
image_use_case = get_image_use_case(use_tensorflow=True, use_transformers=False)

os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN")


DATA_API_ENDPOINT = os.getenv("DATA_API_ENDPOINT")
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/api/process_image', methods=['POST'])
def process_image_route():
    if 'image' not in request.files:
        flash("No image")
        return redirect(request.url)
    
    file = request.files['image']
    if file.filename == '':
        flash("No image")
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        image_text = image_use_case.analyze_image(file_path)
        keyword = image_text[0]
        # dominant_color = analyze_dominant_color(file_path)

        api_data = {
            'keyword': keyword[0],
            'num_elements': 5
        }
        response = requests.post(DATA_API_ENDPOINT, data=api_data)
        descriptions = response.json()
        descriptions_text = json.dumps(descriptions)
        description_string = description_use_case.execute(descriptions_text, keyword)
        return jsonify(description=description_string)
    else:
        flash("File not allowed")
        return redirect(request.url)
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002)

