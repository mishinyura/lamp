from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime

from order_service.core.db import get_session
from order_service.database import user_crud, order_crud
from order_service.schemas import OrderSchema, OrderCreateSchema, UserCreateSchema
from order_service.models import OrderModel, OrderToProductModel, UserModel
from order_service.core.exceptions import SqlException, DuplicateException
from order_service.services.users import user_service
from order_service.services.prodcuts import product_service
from order_service.core.enums import OrderStatus


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
        """Ищем пользователя по номеру телефона"""
        user = await user_service.get_user_by_user_phone(
            user_phone=order_data.user.phone,
            session=session
        )

        if not user:
            user_id = user_service.create_user(order_data.user)
        else:
            user_id = user.id

        """Создаем моедль заказа"""
        order = OrderModel(
            user_id=user_id,
            status=OrderStatus.PENDING,
            total=product_service.get_sum_products(order_data.products),
            created_at=datetime.now()
        )

        try:
            await self.crud.create(order=order, session=session)
        except SqlException as ex:
            await session.rollback()
            raise DuplicateException(message=str(ex))
        else:
            for item in order_data.products:
                product = await product_service.get_product_by_article(item.article, session)

                order_products = OrderToProductModel(
                    order_id=order.id,
                    product_id=product.id,
                    quantity=item.amount,
                )

                await self.crud.create()

            return order.id


order_service = OrderService()
