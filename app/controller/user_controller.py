from app.service.user_service import UserService
from fastapi import APIRouter, Depends, HTTPException, status
from app.schema.user_schema import *
from app.config.database import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()



@router.post("", response_model=UserOut)
def create_user_controller(payload:UserCreate, db:Session = Depends(get_db)):
    service = UserService(db)
    return service.create_user_service(payload)

@router.get("", response_model=List[UserOut])
def get_all_user_controller(db:Session = Depends(get_db)):
    service = UserService(db)
    return service.get_all_user_service()

@router.get("/{email}", response_model=UserOut)
def get_user_email_controller(email:EmailStr, db:Session = Depends(get_db)):
    service = UserService(db)
    return service.get_user_by_email_service(email)

# @router.get("/user/id/{id}", response_model=UserOut)
# def get_User_by_id_controller(id:int, db:Session = Depends(get_db)):
#     service = UserService(db)
#     return service.get_user_by_id_service(id)

@router.put("/{id}", response_model = UserOut)
def update_user_by_id_controller(id:int, payload:UserUpdate ,db:Session = Depends(get_db)):
    service = UserService(db)
    return service.update_user_service(id, payload)

@router.delete("/{id}", response_model=None)
def delete_user_by_id_controller(id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    delete_user = service.delete_user_service(id)
    return {"message": "User deleted successfully"}

