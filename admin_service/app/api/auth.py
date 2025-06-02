from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordRequestForm

from admin_service.app.core.security import create_access_token, authenticate_admin, oauth2_scheme, get_admin, SECRET_KEY, \
    ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

auth_router = APIRouter()


@auth_router.post("/login")
async def login_for_admin(form_data: OAuth2PasswordRequestForm = Depends()):
    admin = authenticate_admin(form_data.username, form_data.password)
    if not admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": admin["username"]},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}


# --- Декоратор для защиты ручек ---
async def get_current_admin(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    admin = get_admin(username)
    if admin is None:
        raise credentials_exception
    return admin


# --- Пример защищённой админ-ручки ---
@auth_router.get("/protected")
async def read_admin(current_admin: dict = Depends(get_current_admin)):
    return {"msg": f"Hello, {current_admin['username']}! This is the admin area."}