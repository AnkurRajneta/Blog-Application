from app.models.user_model import *
from app.config.database import Base 
from app.enums.user_enums import TableName
from sqlalchemy import Column, ForeignKey, Integer, String, INTEGER, Boolean, null, DateTime
from sqlalchemy.orm import relationship



class BlogModel(Base):
    __tablename__ = TableName.BLOG
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_by = Column(ForeignKey(f"{TableName.USER}.id"))
    created_at = Column(DateTime(timezone=True),server_default=func.now(), nullable = True)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(),nullable=True)
    

    user = relationship("User_model", back_populates="blog")
