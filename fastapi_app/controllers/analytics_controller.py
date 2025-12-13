from shared.db.mongo_client import db

analytics_collection = db["analytics"]

def list_analytics():
    return list(analytics_collection.find())
