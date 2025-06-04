from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

from app.database import employee_crud

# Константы конфигурации (секретный ключ, алгоритм, время жизни токена)
SECRET_KEY = "supersecretkey"  # Лучше хранить в .env
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Имитация базы данных админов
# fake_admin_db = {
#     "admin": {
#         "username": "admin",
#         "hashed_password": "$2b$12$KpwJZ5QbdFEOQHK5iHsg2.enQ20O.467wdXHjAhN8Tm0WPvpti.Hm",  # admin123
#     }
# }

# Контекст для хэширования и проверки паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Настройка схемы аутентификации OAuth2 (по токену)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="admin/login")


# Проверка пароля: plain_password — введённый пароль, hashed_password — из базы
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# Аутентификация администратора: проверка наличия и пароля
async def authenticate_admin(username: str, password: str, session: AsyncSession):
    admin = await employee_crud.get(username=username, session=session)
    print('ADMIN', admin.username)
    if not admin:
        return False
    if not verify_password(password, admin.hash_password):
        return False
    return admin


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


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
    admin = None
    print('ADMIN1', token)
    if admin is None:
        raise credentials_exception
    return admin