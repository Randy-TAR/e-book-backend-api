from pydantic import BaseModel
from typing import List, Optional


# ----------- Summarize Book -----------
class SummarizeBookRequest(BaseModel):
    text: str  # extracted text from first 2–3 pages


class SummarizeBookResponse(BaseModel):
    summary: str
    keywords: List[str]


# ----------- Generate Tags -----------
class GenerateTagsRequest(BaseModel):
    title: str
    description: Optional[str] = None


class GenerateTagsResponse(BaseModel):
    tags: List[str]


# ----------- Rewrite Blog -----------
class RewriteBlogRequest(BaseModel):
    content: str
    tone: Optional[str] = "professional"


class RewriteBlogResponse(BaseModel):
    rewritten_content: str


# ----------- AI Search -----------
class AISearchRequest(BaseModel):
    query: str


class AISearchResponse(BaseModel):
    filters: dict
