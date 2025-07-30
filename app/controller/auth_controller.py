from fastapi import HTTPException, APIRouter, status, Depends
from fastapi import security
from sqlalchemy.orm import Session
from app.schema.auth_schema import *

from app.config.database import get_db
from app.service.auth_service import AuthService
from app.middlewares.auth import get_current_user
from app.core.jwt import create_jwt
from fastapi.security import HTTPBearer



router = APIRouter()

security = HTTPBearer()

@router.post('/login')
def login(payload:AuthSchema, db: Session = Depends(get_db)):
    service = AuthService(db)
    user = service.auth_service(payload.email, payload.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect crudentials")
    
    token = create_jwt({"sub":user.email})
    return {"access_token": token, "token_type": "bearer"}
    

@router.post('/register', response_model=RegisterOut)
def register(payload:RegisterSchema, db: Session = Depends(get_db)):
    service = AuthService(db)
    return service.register_auth(payload)


@router.get('/me', dependencies=[Depends(security)])
def me(current_user = Depends(get_current_user)):
    return current_user