from fastapi import APIRouter, Depends
from fastapi_app.core.security import admin_required
from pydantic import BaseModel
from services.ai_services import generate_tags


router = APIRouter(
    prefix="/ai",
    tags=["AI Assistant"]
)

@router.get("/")
def ai_status():
    return {"message": "AI API active"}

@router.get("/logs")
def get_admin_logs(admin=Depends(admin_required)):
    logs = list(db.admin_logs.find({}, {"_id": 0}).sort("timestamp", -1))
    return logs

class SummarizeRequest(BaseModel):
    text: str

@router.post("/summarize-book")
async def summarize_book_endpoint(req: SummarizeRequest):
    return {"summary": "dummy summary", "keywords": ["example"]}


# Request schema
class GenerateTagsRequest(BaseModel):
    text: str

# Response schema
class GenerateTagsResponse(BaseModel):
    tags: list[str]

@router.post("/generate-tags", response_model=GenerateTagsResponse)
async def generate_tags_endpoint(request: GenerateTagsRequest):
    tags = await generate_tags(request.text)
    return {"tags": tags}

