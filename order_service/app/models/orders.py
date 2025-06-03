from sqlalchemy import ForeignKey, Numeric, DateTime, Integer, Enum as AlchemyEnum
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from app.models.base import BaseModel, Base
from app.core.enums import OrderStatus


class OrderModel(BaseModel, Base):
    __tablename__ = 'orders'

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=False)
    total: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    status: Mapped[OrderStatus] = mapped_column(AlchemyEnum(OrderStatus), nullable=False, default=OrderStatus.PENDING)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now())
