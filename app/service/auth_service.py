from app.repository.user_repository import UserRepository
from app.schema.auth_schema import *
from sqlalchemy.orm import Session

class AuthService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def auth_service(self, email, password):
        user = self.repo.get_User_by_email(email)
        if user and user.password == password:
            return user
        return None
    
    def register_auth(self, payload:RegisterSchema):
        new_user = self.repo.create_user(payload)
        return new_user



