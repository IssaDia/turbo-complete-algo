from flask import Flask, request, render_template, flash, redirect, jsonify
import os, sys
sys.path.insert(0, os.path.abspath("../../.."))

from external.replicate.replicate_ai import ReplicateAPI
from providers.ai.image_use_case_provider import get_image_use_case
from use_cases.description_use_case import DescriptionUseCase
from werkzeug.utils import secure_filename

import json
import replicate
import requests

app = Flask(__name__)
app.secret_key = "turbo_complete"

description_use_case = DescriptionUseCase(ReplicateAPI())
image_use_case = get_image_use_case(use_tensorflow=True, use_transformers=False)

os.environ["REPLICATE_API_TOKEN"] = "r8_fG5laWlXKezHHs4KCekQm2tasBesc7S1S4MrX"


DATA_API_ENDPOINT = "http://127.0.0.1:5001/"
OLLAMA_API_ENDPOINT = "http://localhost:11434/api/generate"
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
        prompt_input = f"You are seller on Amazon e-commerce.Generate an attractive product description based on this product : {keyword[0]} with a tone similar to the following product descriptions:\n\n{descriptions_text}"

        ollama_data = {
             'model': "mistral",
            'prompt': prompt_input
        }

        response = requests.post(OLLAMA_API_ENDPOINT, json=ollama_data,  headers={'Content-Type': 'application/json'})
        if response.headers['Content-Type'] == 'application/json':
            json_objects = [json.loads(obj) for obj in response.text.split('\n') if obj.strip() != ""]
            responses = [obj.get('response', '') for obj in json_objects]
            description_string = ' '.join(responses)
            print(description_string)
        else:
            pass
        return jsonify(description=description_string)
    else:
        flash("File not allowed")
        return redirect(request.url)
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002)

