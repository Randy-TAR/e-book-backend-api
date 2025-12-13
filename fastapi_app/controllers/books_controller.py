from shared.db.mongo_client import db
from bson import ObjectId

books = db["books"]

def serialize_book(book):
    return {
        "id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"],
        "description": book["description"],
        "tags": book["tags"],
        "category": book["category"],
        "pdf_url": book["pdf_url"],
        "cover_url": book.get("cover_url")
    }


def add_book(data):
    result = books.insert_one(data)
    new_book = books.find_one({"_id": result.inserted_id})
    return serialize_book(new_book)


def get_all_books():
    return [serialize_book(book) for book in books.find()]


def get_book(book_id):
    book = books.find_one({"_id": ObjectId(book_id)})
    if book:
        return serialize_book(book)
    return None


def update_book(book_id, data):
    books.update_one({"_id": ObjectId(book_id)}, {"$set": data})
    book = books.find_one({"_id": ObjectId(book_id)})
    return serialize_book(book)


def delete_book(book_id):
    books.delete_one({"_id": ObjectId(book_id)})
    return True


def search_books(query):
    return [
        serialize_book(book)
        for book in books.find({
            "$or": [
                {"title": {"$regex": query, "$options": "i"}},
                {"author": {"$regex": query, "$options": "i"}},
                {"tags": {"$regex": query, "$options": "i"}}
            ]
        })
    ]
