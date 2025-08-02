from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user_model import User_model
from app.schema.user_schema import UserCreate, UserOut

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, payload:UserCreate):
        user = User_model(
            name =payload.name,
            email = payload.email,
            password = payload.password )
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user


    async def get_all_user(self):
        get_all = select(User_model)
        result = await self.db.execute(get_all)
        
        return result.scalars().all()

    
    async def get_User_by_email(self, email:str):
        user_email = select(User_model).where(User_model.email == email)
        result = await self.db.execute(user_email)
        return result.scalars().first()

    async def get_user_by_id(self, id:str):
        user_id = select(User_model).where(User_model.id == id)
        result = await self.db.execute(user_id)
        return result.scalars().first()
    
    async def update_user(self, id:str, payload:UserCreate):
        db_update = select(User_model).where(User_model.id ==id)
        result = await self.db.execute(db_update)
        updated =  result.scalars().first()
        updated.name = payload.name
        updated.email = payload.email
        updated.password = payload.password
        await self.db.commit()
        await self.db.refresh(updated)
        return updated
    

    async def delete_user(self, id:int):
        db_delete = select(User_model).where(User_model.id == id)
        result = await self.db.execute(db_delete)
        deleted = result.scalars().first()

        await self.db.delete(deleted)
        await self.db.commit()
        return True


