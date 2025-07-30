from app.models.blog_model import BlogModel
from app.schema.blog_schema import BlogCreate, BlogUpdate
from sqlalchemy.orm import Session
from fastapi import HTTPException

class BlogRepository:
    def __init__(self, db : Session):
        self.db = db

    def create_blog_repository(self,payload:BlogCreate,validated_user_id:int):
        new_blog = BlogModel(title = payload.title,
                             description = payload.description, created_by=validated_user_id)
        
        self.db.add(new_blog)
        self.db.commit()
        self.db.refresh(new_blog)
        return new_blog
    
    def get_blog_repository_all(self):
        return self.db.query(BlogModel).all()
    

    def get_blog_by_id_repository(self, id:int):
        return self.db.query(BlogModel).filter(id == BlogModel.id).first()
    
    def update_blog_by_id_repository(self, id:int, payload:BlogUpdate):
        updated_blog = self.db.query(BlogModel).filter(id == BlogModel.id).first()
        updated_blog.title = payload.title
        updated_blog.description = payload.description
        self.db.commit()
        self.db.refresh(updated_blog)

        return updated_blog
    
    def delete_blog_by_id_repository(self, id:int):
        deleted_value = self.db.query(BlogModel).filter(id == BlogModel.id).first()
        if not deleted_value:
            raise HTTPException(status_code=404, detail="Not Found")
        
        self.db.delete(deleted_value)
        self.db.commit()
        return {"message": "Deleted successfully"}


