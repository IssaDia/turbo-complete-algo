from interfaces.bdd_provider_interface import BDD_PROVIDER_INTERFACE
from external.mongodb.mongo_db_cloud_connection import MongoDB_CONNECTION
from providers.bdd.mongodb.utils import get_documents
from pymongo import errors

class MONGODB_PROVIDER(BDD_PROVIDER_INTERFACE):

    def __init__(self, client_url):
        self._mongodb_client = MongoDB_CONNECTION(client_url)

    def get_descriptions(self):
        try:
            client = self._mongodb_client._client
            db = client.turbo
            collection = db.description
            return get_documents(collection)
        except errors.PyMongoError as e:
            print(f"Error while retrieving descriptions: {e}")
            return []

    def get_images(self):
        try:
            client = self._mongodb_client._client
            db = client.turbo
            collection = db.image
            return get_documents(collection)
        except errors.PyMongoError as e:
            print(f"Error while retrieving images: {e}")
            return []
