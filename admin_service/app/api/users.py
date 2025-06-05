from datetime import timedelta
import json

from fastapi import APIRouter, Depends, HTTPException, status, Form
from fastapi.responses import JSONResponse
from starlette.status import HTTP_409_CONFLICT, HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import create_access_token, authenticate_admin, ACCESS_TOKEN_EXPIRE_MINUTES, get_current_admin
from app.schemas import EmployeeCreateSchema, UserCreateSchema
from app.core.db import get_session
from app.services import user_srv
from app.core.exceptions import DuplicateException

user_router = APIRouter()


@user_router.get('/')
async def get_users(session: AsyncSession = Depends(get_session)):
    users = user_srv.get_all_users(session=session)


@user_router.post("/")
async def get_or_create(
        user_data: UserCreateSchema,
        session: AsyncSession = Depends(get_session)
):
    print("USER", user_data)
    user = await user_srv.get_or_create_user(user_data=user_data, session=session)
    if user:
        return JSONResponse(status_code=HTTP_200_OK, content=user.dict())
    raise HTTPException(status_code=HTTP_404_NOT_FOUND)