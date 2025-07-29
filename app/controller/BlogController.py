from typing import List
from app.service.BlogService import BlogService
from app.schema.BlogSchema import *
from fastapi import APIRouter, Depends, HTTPException, status
from app.config.database import get_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.post('/blog/create', response_model = BlogOut)
def create_blog_controller(payload:BlogCreate, db: Session = Depends(get_db)):
    service = BlogService(db)
    return service.create_blog_service(payload)


@router.get('/blog/all', response_model=List[BlogOut])
def get_blog_controller_all(db: Session = Depends(get_db)):
    service = BlogService(db)
    return service.get_blog_service_all()

@router.get('/blog/{id}', response_model=BlogOut)
def get_blog_by_id_controller(id:int, db: Session = Depends(get_db)):
    service = BlogService(db)
    return service.get_blog_by_id_service(id)


@router.put('/blog/update/{id}', response_model = BlogOut)
def update_blog_by_id_controller(id:int, payload:BlogUpdate,db:Session = Depends(get_db)):
    service = BlogService(db)
    return service.update_blog_by_id_service(id, payload)

@router.delete('/blog/delete/{id}')
def delete_blog_by_id_controller(id: int, db: Session = Depends(get_db)):
    service = BlogService(db)
    delete_blog = service.delete_blog_by_id_service(id)
    return True