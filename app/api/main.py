from flask import Flask, request, render_template, flash, redirect
import os, sys
import requests
import replicate
import json

sys.path.insert(0, os.path.abspath(".."))

from use_cases.use_case_mongo_db import GetDescriptionsUseCase
from external.mongodb.mongo_db_cloud_connection import MongoDB_CONNECTION
from providers.bdd.mongodb.mongodb_provider import MONGODB_PROVIDER

app = Flask(__name__)
app.secret_key = "turbo_complete"

API_ENDPOINT = "http://127.0.0.1:5001/"
os.environ["REPLICATE_API_TOKEN"] = "r8_fG5laWlXKezHHs4KCekQm2tasBesc7S1S4MrX"

CLIENT_URL = os.environ.get("MONGODBCLIENT")
mongo_connection = MongoDB_CONNECTION(CLIENT_URL)
mongodb_provider = MONGODB_PROVIDER(mongo_connection)
get_descriptions_use_case = GetDescriptionsUseCase(mongodb_provider)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')
    
@app.route('/api/process_image', methods=['POST'])
def process_image_route():

    keyword = request.get_data(as_text=True) 
    if keyword:
        api_data = {
                'keyword': keyword,
                'num_elements': 2
        }
        response = requests.post(API_ENDPOINT, data=api_data)
        descriptions = response.json()
        descriptions_text = json.dumps(descriptions)
        print(descriptions_text)
        prompt_input = f"Generate a product description with a tone similar to the following product descriptions:\n\n{descriptions_text}"

        output = replicate.run(
            "meta/llama-2-70b-chat:2d19859030ff705a87c746f7e96eea03aefb71f166725aee39692f1476566d48",
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
        print(description_string, type (description_string))

        test = "This is a test"

        return test

    else:
        flash("File not allowed")
        return redirect(request.url)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002)
