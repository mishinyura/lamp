from sqlalchemy import Column, UUID, String

from app.models.base import BaseModel, Base


class UserModel(Base):
    __tablename__ = 'users'

    uuid = Column(UUID(as_uuid=True), primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String(12), nullable=False)