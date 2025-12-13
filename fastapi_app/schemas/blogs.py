from pydantic import BaseModel
from typing import Optional, List

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
