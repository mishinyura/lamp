from sqlalchemy.ext.asyncio import AsyncSession

from app.database.orders import order_crud
from app.schemas.orders import OrderSchema


class OrderService:
    def __init__(self):
        self.crud = order_crud

    async def get_order(self, order_id: int, session: AsyncSession) -> OrderSchema:
        order = await self.crud.read(order_id, session)
        return order

    async def get_all_orders(self, session: AsyncSession) -> list[OrderSchema]:
        orders = await self.crud.read_all(session=session)
        return orders


order_service = OrderService()
