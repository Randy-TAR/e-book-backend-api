from pydantic import BaseModel
from typing import Optional, List

class BookBase(BaseModel):
    id: str
    title: str
    author: str
    description: str
    tags: List[str]
    category: str
    pdf_url: str

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    category: Optional[str]
