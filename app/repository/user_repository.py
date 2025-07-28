from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user_model import User_model
from app.schema.user_schema import UserCreate, UserOut

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, payload:UserCreate):
        user = User_model(
            name =payload.name,
            email = payload.email,
            password = payload.password )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user


    def get_all_user(self, payload:UserOut):
        self.db.query(User_model).all(payload)

    
    def get_User_by_email(self, email:str):
        self.db.query(User_model).filter(User_model.email == email).first()

    def get_user_by_id(self, id:str):
        self.db.query(User_model).filter(User_model.id == id).first()

    def update_user(self, id:str, payload:UserCreate):
        db_update = self.db.query(User_model).filter(User_model.id == id).first()
        db_update.name = payload.name
        db_update.email = payload.email
        db_update.password = payload.password
        self.db.commit()
        self.db.refresh(db_update)
        return db_update
    

    def delete_user(self, id:int):
        db_delete = self.db.query(User_model).filter(id == User_model.id).first()

        self.db.delete(db_delete)
        self.db.commit()
        return True


