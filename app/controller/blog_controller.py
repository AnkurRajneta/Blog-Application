from typing import List
from app.middlewares.auth_middlewares import get_current_user
from app.models.user_model import User_model
from app.service.blog_service import BlogService
from app.schema.blog_schema import *
from fastapi import APIRouter, Depends, HTTPException, status
from app.config.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post('', response_model = BlogOut)
async def create_blog_controller(payload:BlogCreate, db: AsyncSession = Depends(get_db),current_user:User_model=Depends(get_current_user)):
    service = BlogService(db)
    validated_user_id=current_user.id
    return await service.create_blog_service(payload,validated_user_id)


@router.get('', response_model=List[BlogOut])
async def get_blog_controller_all(db: AsyncSession = Depends(get_db)):
    service = BlogService(db)
    return await service.get_blog_service_all()

@router.get('/{id}', response_model=BlogOut)
async def get_blog_by_id_controller(id:int, db: AsyncSession = Depends(get_db)):
    service = BlogService(db)
    return await service.get_blog_by_id_service(id)


@router.put('/{id}', response_model = BlogOut)
async def update_blog_by_id_controller(id:int, payload:BlogUpdate,db:AsyncSession = Depends(get_db)):
    service = BlogService(db)
    return await service.update_blog_by_id_service(id, payload)

@router.delete('/{id}')
async def delete_blog_by_id_controller(id: int, db: AsyncSession = Depends(get_db)):
    service = BlogService(db)
    delete_blog = await service.delete_blog_by_id_service(id)
    return True