from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status, Form
from fastapi.responses import JSONResponse
from starlette.status import HTTP_409_CONFLICT, HTTP_201_CREATED
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import create_access_token, authenticate_admin, ACCESS_TOKEN_EXPIRE_MINUTES, get_current_admin
from app.schemas import EmployeeCreateSchema
from app.core.db import get_session
from app.services import employee_srv
from app.core.exceptions import DuplicateException

auth_router = APIRouter()


@auth_router.post("/login")
async def login_for_admin(
        form_data: OAuth2PasswordRequestForm = Depends(),
        session: AsyncSession = Depends(get_session)
):
    admin = await authenticate_admin(form_data.username, form_data.password, session=session)
    if not admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": admin.username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}


@auth_router.post('/register', response_class=JSONResponse)
async def register_employee(
        name: str = Form(...),
        username: str = Form(...),
        password: str = Form(...),
        session: AsyncSession = Depends(get_session)
):
    form_data = EmployeeCreateSchema(
        name=name,
        username=username,
        password=password
    )
    try:
        result = await employee_srv.create_new_employee(data=form_data, session=session)
        return JSONResponse(status_code=HTTP_201_CREATED, content=result)
    except DuplicateException as ex:
        raise HTTPException(status_code=HTTP_409_CONFLICT, detail=str(ex))


@auth_router.get("/protected")
async def read_admin(
        current_admin: dict = Depends(get_current_admin)
):
    return {"msg": f"Hello, {current_admin}! This is the admin area."}