from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Depends
from ..controllers import books_controller
import shutil, os
from uuid import uuid4
from fastapi import Query
from fastapi_app.schemas.books import BookCreate
from fastapi_app.core.security import admin_required
from fastapi_app.utils.admin_logger import log_admin_action

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

UPLOAD_DIR = "uploads/books/"
COVER_DIR = "uploads/covers/"


# ------------------------------------------
# Upload Book
# ------------------------------------------
# @router.post("/upload", dependencies=[Depends(admin_required)])
# def upload_book(
#     title: str = Form(...),
#     author: str = Form(...),
#     description: str = Form(...),
#     category: str = Form(...),
#     tags: str = Form(...),
#     pdf_file: UploadFile = File(...),
#     cover_image: UploadFile = File(None)
# ):
#     # Save PDF
#     pdf_filename = f"{uuid4()}_{pdf_file.filename}"
#     pdf_path = os.path.join(UPLOAD_DIR, pdf_filename)

#     with open(pdf_path, "wb") as buffer:
#         shutil.copyfileobj(pdf_file.file, buffer)

#     # Save cover image (optional)
#     cover_url = None
#     if cover_image:
#         cover_filename = f"{uuid4()}_{cover_image.filename}"
#         cover_path = os.path.join(COVER_DIR, cover_filename)

#         with open(cover_path, "wb") as buffer:
#             shutil.copyfileobj(cover_image.file, buffer)

#         cover_url = cover_path

#     # Prepare data for DB
#     data = {
#         "title": title,
#         "author": author,
#         "description": description,
#         "category": category,
#         "tags": tags.split(","),
#         "pdf_url": pdf_path,
#         "cover_url": cover_url,
#     }

#     return books_controller.add_book(data)


# ------------------------------------------
# Get All Books
# ------------------------------------------
# @router.get("/")
# def list_books():
#     return books_controller.get_all_books()
@router.get("/")
def list_books(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=50)
):
    return books_controller.get_all_books(page, limit)

# ------------------------------------------
# Get Single Book
# ------------------------------------------
@router.get("/{book_id}")
def get_book(book_id: str):
    book = books_controller.get_book(book_id)
    if not book:
        raise HTTPException(404, "Book not found")
    return book


# ------------------------------------------
# Search Books
# ------------------------------------------
@router.get("/search/{query}")
def search(query: str):
    return books_controller.search_books(query)


# ------------------------------------------
# Download Book
# ------------------------------------------
@router.get("/download/{book_id}")
def download_book(book_id: str):
    book = books_controller.get_book(book_id)
    if not book:
        raise HTTPException(404, "Book not found")

    return {
        "download_url": f"/{book['pdf_url']}"
    }


# ------------------------------------------
# Read Online (Stream PDF)
# ------------------------------------------
from fastapi.responses import FileResponse

@router.get("/read/{book_id}")
def read_online(book_id: str):
    book = books_controller.get_book(book_id)
    if not book:
        raise HTTPException(404, "Book not found")

    return FileResponse(book["pdf_url"], media_type="application/pdf")


# ------------------------------------------
# Update Book
# ------------------------------------------
@router.put("/{book_id}", dependencies=[Depends(admin_required)])
def update_book(book_id: str, title: str = Form(None), author: str = Form(None),
                description: str = Form(None), category: str = Form(None),
                tags: str = Form(None)):
    update_data = {}
    if title: update_data["title"] = title
    if author: update_data["author"] = author
    if description: update_data["description"] = description
    if category: update_data["category"] = category
    if tags: update_data["tags"] = tags.split(",")

    return books_controller.update_book(book_id, update_data)


# ------------------------------------------
# Delete Book
# ------------------------------------------
# @router.delete("/{book_id}", dependencies=[Depends(admin_required)])
# def delete_book(book_id: str):
#     books_controller.delete_book(book_id)
#     return {"message": "Book deleted"}


# ------------------------------------------
# Create Book
# ------------------------------------------
@router.post("/")
def create_book(book: BookCreate, admin=Depends(admin_required)):
    result = db.books.insert_one(book.dict())

    log_admin_action(
        admin=admin,
        action="BOOK_CREATED",
        resource_id=str(result.inserted_id)
    )

    return {"message": "Book created"}


# ------------------------------------------
# Delete Book
# ------------------------------------------
@router.delete("/{book_id}")
def delete_book(book_id: str, admin=Depends(admin_required)):
    db.books.delete_one({"_id": ObjectId(book_id)})

    log_admin_action(
        admin=admin,
        action="BOOK_DELETED",
        resource_id=book_id
    )

    return {"message": "Book deleted"}
