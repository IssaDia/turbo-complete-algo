import requests
import os
import json

# os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN")
OLLAMA_API_ENDPOINT =  os.getenv("OLLAMA_API_ENDPOINT")
OLLAMA_API_ENDPOINT = "http://localhost:11434/api/generate"


class ReplicateAPI:
    def __init__(self):
        pass

    def generate_description(self, descriptions_text, keyword):
        # Construction de la phrase d'entrée pour l'API OLLAMA en utilisant le texte fourni et le mot-clé
        prompt_input = f"As a seller on Amazon's e-commerce platform, you want to generate an irresistible product description for your {keyword[0]}. Craft a compelling and attractive description with a tone similar to the following product descriptions:\n\n{descriptions_text}"

        # Construction des données à envoyer à l'API OLLAMA
        ollama_data = {
             'model': "mistral",
            'prompt': prompt_input
        }
        # Envoi d'une requête POST à l'API OLLAMA avec les données spécifiées

        response = requests.post(OLLAMA_API_ENDPOINT, json=ollama_data,  headers={'Content-Type': 'application/json'})

        # Traitement des données renvoyées par l'API OLLAMA
        json_objects = [json.loads(obj) for obj in response.text.split('\n') if obj.strip() != ""]
        responses = [obj.get('response', '') for obj in json_objects]

        # Affichage des données renvoyées par l'API OLLAMA
        description_string = ' '.join(responses)

        return description_string
