from pymongo import errors

def insert_documents(collection, documents):
    try:
        for document in documents:
            collection.insert_one(document)
        print("Documents successfully inserted")
    except errors.PyMongoError as e:
        print(f"Error: {e}")

def get_documents(collection):
    try:
        documents = []
        for document_dict in collection.find({}):
            # Convert MongoDB document to your entity
            print(document_dict)
            document = {
                key: document_dict[key] for key in document_dict
            }
            documents.append(document)
        return documents
    except errors.PyMongoError as e:
        print(f"Error: {e}")
        return []
