from shared.db.mongo_client import db
from bson import ObjectId
from datetime import datetime

blogs_collection = db["blogs"]

def create_blog(data: dict):
    data["created_at"] = datetime.utcnow()
    result = blogs_collection.insert_one(data)
    return str(result.inserted_id)

def get_all_blogs():
    blogs = []
    for blog in blogs_collection.find():
        blog["id"] = str(blog["_id"])
        del blog["_id"]
        blogs.append(blog)
    return blogs

def get_all_blogs_paginated(page: int = 1, limit: int = 10):
    skip = (page - 1) * limit

    total = blogs_collection.count_documents({})
    blogs = []

    for blog in blogs_collection.find().skip(skip).limit(limit):
        blog["id"] = str(blog["_id"])
        del blog["_id"]
        blogs.append(blog)

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "data": blogs
    }


def get_blog(blog_id: str):
    blog = blogs_collection.find_one({"_id": ObjectId(blog_id)})
    if blog:
        blog["id"] = str(blog["_id"])
        del blog["_id"]
        return blog
    return None

def update_blog(blog_id: str, data: dict):
    blogs_collection.update_one(
        {"_id": ObjectId(blog_id)},
        {"$set": data}
    )

def delete_blog(blog_id: str):
    blogs_collection.delete_one({"_id": ObjectId(blog_id)})

def search_blogs(keyword: str):
    results = []
    query = {
        "$or": [
            {"title": {"$regex": keyword, "$options": "i"}},
            {"content": {"$regex": keyword, "$options": "i"}},
            {"tags": {"$in": [keyword]}}
        ]
    }

    for blog in blogs_collection.find(query):
        blog["id"] = str(blog["_id"])
        del blog["_id"]
        results.append(blog)

    return results

# def list_blogs():
#     return list(blogs_collection.find())
