from shared.db.mongo_client import db

blogs_collection = db["blogs"]

def list_blogs():
    return list(blogs_collection.find())
