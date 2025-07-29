from click import DateTime, Option
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class BlogCreate(BaseModel):
    title: str = Field(min_length=2, example="FastAPI")
    description: str = Field(min_length=10, example ="Currently working on FastAPI")
    
    

class BlogUpdate(BaseModel):
    title:Optional[str] = Field(None, min_length=2, example = "Backend")
    description:Optional[str] = Field(None, min_length=10, example="Currently learning Backend")




class BlogOut(BaseModel):
    id: int
    title : str
    description: str
    created_by:Optional[int] = None
    created_at:datetime
    updated_at:datetime

    class Config:
        from_attributes = True
