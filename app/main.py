from fastapi import FastAPI
from app.config.database import Base, engine
from app.models import *
from app.controller.UserController import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Blog API",
    version="1.0.0"
)

app.include_router(user_router, prefix="/user", tags=["User"])



