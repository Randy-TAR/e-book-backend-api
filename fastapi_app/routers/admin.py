from fastapi import APIRouter, Depends
from fastapi_app.core.security import admin_required
from shared.db.mongo_client import db  # Your MongoDB client

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

@router.get("/stats", dependencies=[Depends(admin_required)])
def get_admin_stats():
    books_count = db.books.count_documents({})
    blogs_count = db.blogs.count_documents({})
    
    # For simplicity, assume each book document has a "downloads" field
    total_downloads = 0
    for book in db.books.find({}, {"downloads": 1}):
        total_downloads += book.get("downloads", 0)

    return {
        "total_books": books_count,
        "total_blogs": blogs_count,
        "total_downloads": total_downloads
    }
