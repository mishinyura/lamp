from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from datetime import datetime

from app.core.enums import OrderStatus


class OrderSchema(BaseModel):
    id: int
    user_id: int
    status: OrderStatus
    total: Decimal
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserInOrder(BaseModel):
    name: str
    phone: str


class ProductInOrder(BaseModel):
    article: str
    amount: int


class OrderCreateSchema(BaseModel):
    user: UserInOrder
    products: list[ProductInOrder]

    model_config = {
        "arbitrary_types_allowed": True
    }