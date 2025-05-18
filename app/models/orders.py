from sqlalchemy import Column, UUID, ForeignKey, Numeric, DateTime, Enum as AlchemyEnum
from datetime import datetime

from app.models.base import BaseModel, Base
from app.core.enums import OrderStatus


class OrderModel(BaseModel, Base):
    __tablename__ = 'orders'

    user_id = Column(UUID, ForeignKey('users.uuid'), nullable=False)
    total = Column(Numeric(10, 2), nullable=False)
    status = Column(AlchemyEnum(OrderStatus), nullable=False, default=OrderStatus.PENDING)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
