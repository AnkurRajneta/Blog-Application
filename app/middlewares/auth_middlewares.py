# app/middlewares/auth_middlewares.py

from fastapi import Header, HTTPException, Request, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.config.database import get_db
from app.repository.user_repository import UserRepository
from app.utils.jwt_utils import decode_jwt
from fastapi.concurrency import run_in_threadpool

async def get_current_user(
    request: Request,
    db: AsyncSession = Depends(get_db)
):
    authorization = request.headers.get('Authorization')

    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing or invalid Authorization header"
        )

    token = authorization[7:].strip()
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Empty token in Authorization header"
        )

    try:
        payload = decode_jwt(token)  # ✅ Use threadpool to avoid blocking
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid or expired token: {str(e)}"
        )

    email = payload.get("sub")
    if not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token missing subject (sub) claim"
        )

    try:
        user = await UserRepository(db).get_User_by_email(email)
    except Exception as db_exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error while accessing user data"
        )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user
