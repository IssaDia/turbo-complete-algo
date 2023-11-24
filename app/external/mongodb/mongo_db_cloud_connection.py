from pymongo import MongoClient, errors

class MongoDB_CONNECTION():

    _instance = None

    def __new__(cls, client_url):
        if cls._instance is None:
            try:
                cls._instance = super().__new__(cls)
                cls._instance._client = MongoClient(client_url)
                print('Database Connection Established........')
            except errors.PyMongoError as e:
                print(f"Couldn't connect to Database: {e}")
        return cls._instance
