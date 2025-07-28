from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    name:str = Field(min_length=3, max_length=50, example="Ankur Rajneta")
    email:EmailStr = Field(example="ankurrajneta@gmail.com")
    password:str = Field(min_length=5, example = "strongpassword")


class UserUpdate(BaseModel):
    name : Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = Field(None)
    password:Optional[str] = Field(None, min_length=5, example = "strongPassword")


class UserOut(BaseModel):
    id:int
    name:str
    email:EmailStr
    created_at : datetime
    updated_at : datetime
    is_active: bool
    created_by: Optional[int] = None
    updated_by: Optional[int] = None

    class Config:
        from_attributes = True