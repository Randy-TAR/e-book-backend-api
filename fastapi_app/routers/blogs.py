# from fastapi import APIRouter

# router = APIRouter(
#     prefix="/blogs",
#     tags=["Blogs"]
# )

# @router.get("/")
# def get_blogs():
#     return {"message": "Blogs endpoint working"}

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse
from typing import Optional
import uuid
import os
from fastapi import Query
from ..controllers import blogs_controller

router = APIRouter(prefix="/blogs", tags=["Blogs"])

UPLOAD_DIR = "uploads/blogs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/create")
async def create_blog(
    title: str = Form(...),
    content: str = Form(...),
    tags: str = Form(""),
    image: Optional[UploadFile] = File(None)
):
    image_path = None

    if image:
        filename = f"{uuid.uuid4()}_{image.filename}"
        image_path = f"{UPLOAD_DIR}/{filename}"
        with open(image_path, "wb") as f:
            f.write(await image.read())

    blog_data = {
        "title": title,
        "content": content,
        "tags": [tag.strip() for tag in tags.split(",") if tag],
        "image": image_path
    }

    blog_id = blogs_controller.create_blog(blog_data)
    return {"message": "Blog created", "id": blog_id}


# @router.get("/")
# def list_blogs():
#     return blogs_controller.get_all_blogs()
@router.get("/")
def list_blogs(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=50)
):
    return blogs_controller.get_all_blogs_paginated(page, limit)


@router.get("/{blog_id}")
def get_blog(blog_id: str):
    blog = blogs_controller.get_blog(blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog


@router.get("/search/{keyword}")
def search(keyword: str):
    return blogs_controller.search_blogs(keyword)


@router.put("/{blog_id}")
def update_blog(
    blog_id: str,
    title: Optional[str] = Form(None),
    content: Optional[str] = Form(None),
    tags: Optional[str] = Form(None)
):
    update_data = {}
    if title:
        update_data["title"] = title
    if content:
        update_data["content"] = content
    if tags:
        update_data["tags"] = [t.strip() for t in tags.split(",")]

    blogs_controller.update_blog(blog_id, update_data)
    return {"message": "Blog updated"}


@router.delete("/{blog_id}")
def delete_blog(blog_id: str):
    blogs_controller.delete_blog(blog_id)
    return {"message": "Blog deleted"}
