from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from order_service.models.base import BaseModel, Base


class UserModel(BaseModel, Base):
    __tablename__ = 'users'

    name: Mapped[str] = mapped_column(String, nullable=False)
    phone: Mapped[str] = mapped_column(String(12), nullable=False)