from fastapi import APIRouter

router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"]
)

@router.get("/")
def get_blogs():
    return {"message": "Blogs endpoint working"}
