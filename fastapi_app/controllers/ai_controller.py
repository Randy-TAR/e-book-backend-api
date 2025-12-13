from shared.db.mongo_client import db

ai_collection = db["ai"]

def list_ai():
    return list(ai_collection.find())
