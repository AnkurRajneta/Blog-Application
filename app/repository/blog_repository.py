from sqlalchemy.orm import selectinload  # ✅ Import selectinload
from sqlalchemy import select
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.blog_model import BlogModel
from app.schema.blog_schema import BlogCreate, BlogUpdate

class BlogRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_blog_repository(self, payload: BlogCreate, validated_user_id: int):
        new_blog = BlogModel(
            title=payload.title,
            description=payload.description,
            created_by=validated_user_id
        )
        self.db.add(new_blog)
        await self.db.commit()
        await self.db.refresh(new_blog)
        return new_blog

    async def get_blog_repository_all(self):
        stmt = select(BlogModel).options(selectinload(BlogModel.user))  # ✅ Eagerly load user
        result = await self.db.execute(stmt)
        return result.scalars().all()

    async def get_blog_by_id_repository(self, id: int):
        stmt = select(BlogModel).where(BlogModel.id == id).options(selectinload(BlogModel.user))  # ✅ Eagerly load user
        result = await self.db.execute(stmt)
        return result.scalars().first()

    async def update_blog_by_id_repository(self, id: int, payload: BlogUpdate):
        stmt = select(BlogModel).options(selectinload(BlogModel.user)).where(BlogModel.id == id)
        result = await self.db.execute(stmt)
        updated_result = result.scalars().first()

        if not updated_result:
            raise HTTPException(status_code=404, detail="Blog not found")

        updated_result.title = payload.title
        updated_result.description = payload.description
        await self.db.commit()
        await self.db.refresh(updated_result)
        return updated_result

    async def delete_blog_by_id_repository(self, id: int):
        stmt = select(BlogModel).where(BlogModel.id == id)
        result = await self.db.execute(stmt)
        deleted_item = result.scalars().first()

        if not deleted_item:
            raise HTTPException(status_code=404, detail="Blog not found")

        await self.db.delete(deleted_item)
        await self.db.commit()
        return {"message": "Deleted successfully"}
