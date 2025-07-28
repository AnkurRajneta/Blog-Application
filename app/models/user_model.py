from sqlalchemy import Column, String, Integer, DateTime, func, Boolean

from app.config.database import Base
from app.enums.user_enums import TableName

class User_model(Base):
    __tablename__ = TableName.USER
    id = Column(Integer, primary_key=True) 
    name = Column(String, nullable = False)
    email = Column(String, nullable= False)
    password = Column(String, nullable= False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable = True)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(),onupdate = func.now(), nullable= True)
    isActive = Column(Boolean, nullable=False)
    created_by = Column(Integer, nullable= False)
    updated_by = Column(Integer, nullable= False)