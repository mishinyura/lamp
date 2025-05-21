from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_session
from app.database.orders import order_crud
from app.schemas.orders import OrderSchema, OrderCreateSchema
from app.models import OrderModel, OrderToProductModel
from app.core.exceptions import SqlException, DuplicateException


class OrderService:
    def __init__(self):
        self.crud = order_crud

    async def get_order(self, order_id: int, session: AsyncSession) -> OrderSchema:
        order = await self.crud.read(order_id, session)
        return order

    async def get_all_orders(self, session: AsyncSession) -> list[OrderSchema]:
        orders = await self.crud.read_all(session=session)
        return orders

    async def create_order(
            self, order_data: OrderCreateSchema, session: AsyncSession
    ):
        order = OrderModel(
            user_id=order_data.user_id,
            status=order_data.status,
            total=order_data.total
        )
        order_products = OrderToProductModel(

        )
        try:
            await self.crud.create(order=order, session=session)
        except SqlException as ex:
            raise DuplicateException(message=str(ex))


order_service = OrderService()
