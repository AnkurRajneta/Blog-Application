from app.service.UserService import UserService
from fastapi import APIRouter, Depends, HTTPException, status
from app.schema.user_schema import *
from app.config.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()
class UserController:
    def __init__(self, db:Session):
        self.service = UserService(db)


    @router.post("/user/1.1", response_model=UserOut)
    def create_user_controller(self,payload:UserCreate, db:Session = Depends(get_db)):
        return self.service.create_user_service(payload)
    
    @router.get("/user/all/1.2", response_model=UserOut)
    def get_all_user_controller(self, db:Session = Depends(get_db)):
        return self.service.get_all_user_service()
    
    @router.get("/user/email/1.3", response_model=UserOut)
    def get_user_email_controller(self, email:EmailStr, db:Session = Depends(get_db)):
        return self.service.get_user_by_email_service(email)
    
    @router.get("/user/id/1.4", response_model=UserOut)
    def get_User_by_id_controller(self, id:int, db:Session = Depends(get_db)):
        return self.service.ge
        

