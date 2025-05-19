from pydantic import BaseModel
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
