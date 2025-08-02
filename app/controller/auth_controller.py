from fastapi import HTTPException, APIRouter, status, Depends
from fastapi import security
from sqlalchemy.ext.asyncio import AsyncSession
from app.schema.auth_schema import *

from app.config.database import get_db
from app.service.auth_service import AuthService
from app.middlewares.auth_middlewares import get_current_user
from app.utils.jwt_utils import create_jwt
from fastapi.security import HTTPBearer



router = APIRouter()

security = HTTPBearer()


@router.post('/login')
async def login(payload:AuthSchema, db: AsyncSession = Depends(get_db)):
    service = AuthService(db)
    user = await service.auth_service(payload.email, payload.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect crudentials")
    
    token =  create_jwt({"sub":user.email})
    return {"access_token": token, "token_type": "bearer"}
    

@router.post('/register', response_model=RegisterOut)
async def register(payload:RegisterSchema, db: AsyncSession = Depends(get_db)):
    service = AuthService(db)
    return await service.register_auth(payload)


@router.get('/me')
def me(current_user = Depends(get_current_user)):
    return current_user