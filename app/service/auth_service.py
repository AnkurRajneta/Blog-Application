from app.repository.user_repository import UserRepository
from app.schema.auth_schema import *
from sqlalchemy.ext.asyncio import AsyncSession

class AuthService:
    def __init__(self, db: AsyncSession):
        self.repo = UserRepository(db)

    async def auth_service(self, email, password):
        user = await self.repo.get_User_by_email(email)
        if user and user.password == password:
            return user
        return None
    
    async def register_auth(self, payload:RegisterSchema):
        new_user = await self.repo.create_user(payload)
        return new_user



