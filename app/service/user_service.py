from app.repository.user_repository import UserRepository
from app.schema.user_schema import *
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
class UserService:
    def __init__(self, db:AsyncSession):
        self.repo = UserRepository(db)

    async def create_user_service(self, payload:UserCreate):
        new_user = await self.repo.create_user(payload)
        return new_user

    async def get_all_user_service(self):
        return await self.repo.get_all_user()
    
    async def get_user_by_email_service(self,email:str):
        return await self.repo.get_User_by_email(email)
    
    async def get_user_by_id_service(self, id:int):
        return await self.repo.get_user_by_id(id)
    
    async def update_user_service(self, id:int, payload:UserUpdate):
        return await self.repo.update_user(id, payload)
    
    async def delete_user_service(self, id:int):
        return await self.repo.delete_user(id)
    


    
