from app.repository.user_repository import UserRepository
from app.schema.user_schema import *
from fastapi import HTTPException
from sqlalchemy.orm import Session 

class UserService:
    def __init__(self, db:Session):
        self.repo = UserRepository(db)

    def create_user_service(self, payload:UserCreate):
        new_user = self.repo.create_user(payload)
        return new_user

    def get_all_user_service(self):
        return self.repo.get_all_user()
    
    def get_user_by_email_service(self,email:str):
        return self.repo.get_User_by_email(email)
    
    def get_user_by_id_service(self, id:int):
        return self.repo.get_user_by_id(id)
    
    def update_user_service(self, id:int, payload:UserUpdate):
        return self.repo.update_user(id, payload)
    
    def delete_user_service(self, id:int):
        return self.repo.delete_user(id)
    


    
