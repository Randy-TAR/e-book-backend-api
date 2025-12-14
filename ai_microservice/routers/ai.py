from fastapi import APIRouter
from models.ai_models import (
    SummarizeBookRequest,
    SummarizeBookResponse,
    GenerateTagsRequest,
    GenerateTagsResponse,
    RewriteBlogRequest,
    RewriteBlogResponse,
    AISearchRequest,
    AISearchResponse,
)

router = APIRouter(prefix="/ai", tags=["AI"])


# 1️⃣ Summarize Book
@router.post("/summarize-book", response_model=SummarizeBookResponse)
def summarize_book(payload: SummarizeBookRequest):
    return {
        "summary": payload.text[:200] + "...",
        "keywords": ["education", "technology", "learning"]
    }


# 2️⃣ Generate Tags
@router.post("/generate-tags", response_model=GenerateTagsResponse)
def generate_tags(payload: GenerateTagsRequest):
    return {
        "tags": ["ebook", "programming", "ai"]
    }


# 3️⃣ Rewrite Blog
@router.post("/rewrite-blog", response_model=RewriteBlogResponse)
def rewrite_blog(payload: RewriteBlogRequest):
    rewritten = f"[{payload.tone.upper()} VERSION]\n\n{payload.content}"
    return {
        "rewritten_content": rewritten
    }


# 4️⃣ AI Search
@router.post("/search", response_model=AISearchResponse)
def ai_search(payload: AISearchRequest):
    return {
        "filters": {
            "keywords": payload.query.split(),
            "sort": "relevance"
        }
    }
