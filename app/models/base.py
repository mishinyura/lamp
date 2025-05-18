from sqlalchemy import Integer, Column
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class BaseModel:
    id = Column(Integer, primary_key=True, index=True)