from fastapi import APIRouter

router = APIRouter(
    prefix="/ai",
    tags=["AI Assistant"]
)

@router.get("/")
def ai_status():
    return {"message": "AI API active"}
