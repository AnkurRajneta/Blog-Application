from app.repository.blog_repository import BlogRepository
from app.schema.blog_schema import *
# from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession


class BlogService:
    def __init__(self, db: AsyncSession):
        self.repo = BlogRepository(db)

    async def create_blog_service(self, payload:BlogCreate, validated_user_id:int):
        return await self.repo.create_blog_repository(payload,validated_user_id)
    
    async def get_blog_service_all(self):
        return await self.repo.get_blog_repository_all()
    

    async def get_blog_by_id_service(self, id):
        return await self.repo.get_blog_by_id_repository(id)
    

    async def update_blog_by_id_service(self, payload:BlogUpdate, id:int):
        return await self.repo.update_blog_by_id_repository(payload, id)
    
    async def delete_blog_by_id_service(self, id:int):
        return await self.repo.delete_blog_by_id_repository(id)