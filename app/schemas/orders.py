from pydantic import BaseModel, ConfigDict
from uuid import UUID
from decimal import Decimal
from datetime import datetime

from app.core.enums import OrderStatus


class OrderSchema(BaseModel):
    id: int
    user_id: UUID
    status: OrderStatus
    total: Decimal
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class OrderCreateSchema(BaseModel):
    user_id: UUID
    products: list
    total: Decimal