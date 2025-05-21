from sqlalchemy import Column, String, Integer

from app.models.base import BaseModel, Base


class UserModel(BaseModel, Base):
    __tablename__ = 'users'

    name = Column(String, nullable=False)
    phone = Column(String(12), nullable=False)