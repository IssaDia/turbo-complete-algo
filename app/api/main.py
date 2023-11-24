from flask import Flask, request, render_template, flash, redirect
import os, sys
import requests
import replicate
from transformers import pipeline
import json

sys.path.insert(0, os.path.abspath(".."))

from ai.color_model import analyze_dominant_color
from ai.image_description import predict_product_category
from use_cases.use_case_mongo_db import GetDescriptionsUseCase
from external.mongodb.mongo_db_cloud_connection import MongoDB_CONNECTION
from providers.bdd.mongodb.mongodb_provider import MONGODB_PROVIDER
from providers.ai.image_use_case_provider import get_image_use_case
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.secret_key = "turbo_complete"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

API_ENDPOINT = "http://127.0.0.1:5001/"
os.environ["REPLICATE_API_TOKEN"] = "r8_fG5laWlXKezHHs4KCekQm2tasBesc7S1S4MrX"

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

CLIENT_URL = os.environ.get("MONGODBCLIENT")
mongo_connection = MongoDB_CONNECTION(CLIENT_URL)
mongodb_provider = MONGODB_PROVIDER(mongo_connection)
get_descriptions_use_case = GetDescriptionsUseCase(mongodb_provider)


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
        image_use_case = get_image_use_case(use_tensorflow=False, use_transformers=True)
        image_text = image_use_case.analyze_image(file_path)
        keyword = predict_product_category(file_path)[0]
        dominant_color = analyze_dominant_color(file_path)

        api_data = {
            'keyword' : keyword[0],
            'num_elements' : 5
        }
        response = requests.post(API_ENDPOINT, data=api_data)
        descriptions = response.json()
        descriptions_text = json.dumps(descriptions)
        prompt_input = f"Generate a product description with a tone similar to the following product descriptions:\n\n{descriptions_text}"

        output = replicate.run(
            "meta/llama-2-7a0b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
            input={
                "debug": False,
                "top_k": 50,
                "top_p": 1,
                "prompt": prompt_input,
                "temperature": 0.5,
                "max_new_tokens": 500,
                "min_new_tokens": -1
            }
        )
        output_list = list(output)
        description_string = ''.join(output_list)
        print(description_string)


        return render_template('success_image.html', image_text=image_text)
    else:
        flash("File not allowed")
        return redirect(request.url)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002)
