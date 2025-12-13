from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class BlogBase(BaseModel):
    title: str
    content: str
    tags: List[str]

class BlogCreate(BlogBase):
    pass

class BlogUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]
    tags: Optional[List[str]]

class BlogResponse(BaseModel):
    id: str
    title: str
    content: str
    tags: List[str]
    image: Optional[str]
    created_at: datetime
