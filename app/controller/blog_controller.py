from typing import List
from app.middlewares.auth_middlewares import get_current_user
from app.models.user_model import User_model
from app.service.blog_service import BlogService
from app.schema.blog_schema import *
from fastapi import APIRouter, Depends, HTTPException, status
from app.config.database import get_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.post('', response_model = BlogOut)
def create_blog_controller(payload:BlogCreate, db: Session = Depends(get_db),current_user:User_model=Depends(get_current_user)):
    service = BlogService(db)
    validated_user_id=current_user.id
    return service.create_blog_service(payload,validated_user_id)


@router.get('', response_model=List[BlogOut])
def get_blog_controller_all(db: Session = Depends(get_db)):
    service = BlogService(db)
    return service.get_blog_service_all()

@router.get('/{id}', response_model=BlogOut)
def get_blog_by_id_controller(id:int, db: Session = Depends(get_db)):
    service = BlogService(db)
    return service.get_blog_by_id_service(id)


@router.put('/{id}', response_model = BlogOut)
def update_blog_by_id_controller(id:int, payload:BlogUpdate,db:Session = Depends(get_db)):
    service = BlogService(db)
    return service.update_blog_by_id_service(id, payload)

@router.delete('/{id}')
def delete_blog_by_id_controller(id: int, db: Session = Depends(get_db)):
    service = BlogService(db)
    delete_blog = service.delete_blog_by_id_service(id)
    return True