from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

# from app.exceptions import SqlException
from app.models.orders import OrderModel
from app.schemas.orders import OrderSchema
from app.database.base_crud import BaseCrud


class OrderCrud(BaseCrud):
    async def get(self, elem):
        pass

    async def get_all(self, session: AsyncSession) -> list[OrderSchema]:
        result = await session.execute(select(OrderModel))
        orders = result.scalars().all()
        return [OrderSchema.model_validate(order) for order in orders]

    async def add(self, order: OrderModel, session: AsyncSession) -> None:
        try:
            session.add(order)
            await session.commit()
        except SQLAlchemyError as exc:
            await session.rollback()
            # raise SqlException(message=str(exc))

    # async def get_payment_by_payment_id(
    #     self, payment_id: str, session: AsyncSession
    # ) -> PaymentSchema | None:
    #     result = await session.execute(
    #         select(Payment).where(Payment.payment_id == payment_id)
    #     )
    #     data = result.scalars().one_or_none()
    #     if not data:
    #         return None
    #     return PaymentSchema.model_validate(data)
    #
    # async def update_payment_status(
    #     self, payment_id: str, payment_status: str, session: AsyncSession
    # ) -> None:
    #     try:
    #         await session.execute(
    #             update(Payment)
    #             .where(Payment.payment_id == payment_id)
    #             .values(payment_status=payment_status)
    #         )
    #         await session.commit()
    #     except SQLAlchemyError as exc:
    #         await session.rollback()
    #         raise SqlException(message=str(exc))


order_crud = OrderCrud()