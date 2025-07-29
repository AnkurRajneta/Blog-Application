from app.repository.BlogRepository import BlogRepository
from app.schema.BlogSchema import *
from sqlalchemy.orm import Session


class BlogService:
    def __init__(self, db: Session):
        self.repo = BlogRepository(db)

    def create_blog_service(self, payload:BlogCreate):
        return self.repo.create_blog_repository(payload)
    
    def get_blog_service_all(self):
        return self.repo.get_blog_repository_all()
    

    def get_blog_by_id_service(self, id):
        return self.repo.get_blog_by_id_repository(id)
    

    def update_blog_by_id_service(self, payload:BlogUpdate, id:int):
        return self.repo.update_blog_by_id_repository(payload, id)
    
    def delete_blog_by_id_service(self, id:int):
        return self.repo.delete_blog_by_id_repository(id)