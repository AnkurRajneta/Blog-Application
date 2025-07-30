from pydantic import BaseModel, EmailStr
from typing import Optional

class AuthSchema(BaseModel):
    email: EmailStr
    password: str


class RegisterSchema(BaseModel):
    name: Optional[str] = None
    email:EmailStr
    password:str

class RegisterOut(BaseModel):
    id : int
    email: EmailStr
    
    class Config:
        from_attributes = True