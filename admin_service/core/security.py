from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

SECRET_KEY = "supersecretkey"  # Лучше вынести в .env!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_admin_db = {
    "admin": {
        "username": "admin",
        "hashed_password": "$2b$12$KpwJZ5QbdFEOQHK5iHsg2.enQ20O.467wdXHjAhN8Tm0WPvpti.Hm", # password: admin123
    }
}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="admin/login")


def verify_password(plain_password, hashed_password):
    from passlib.context import CryptContext
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    try:
        result = pwd_context.verify(plain_password, hashed_password)
        print("verify result:", result)
        return result
    except Exception as e:
        print("Verify exception:", e)
        return False


def get_admin(username: str):
    admin = fake_admin_db.get(username)
    return admin


def authenticate_admin(username: str, password: str):
    admin = get_admin(username)
    print("admin:", admin)
    print("username from input:", username)
    print("password from input:", password)
    if not admin:
        print("no such admin")
        return False
    if not verify_password(password, admin["hashed_password"]):
        print("Password verification failed")
        print("password:", password)
        print("hashed_password:", admin["hashed_password"])
        return False
    print("Password correct")
    return admin


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)