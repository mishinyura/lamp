from abc import ABC

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from app.core.exceptions import SqlException
from app.models import ProductModel
from app.schemas import ProductSchema
from app.database.base_crud import BaseCrud


class ProductCRUD(BaseCrud, ABC):
    async def create(self, product: ProductModel, session: AsyncSession) -> None:
        try:
            session.add(product)
            await session.commit()
        except SQLAlchemyError as exc:
            await session.rollback()
            raise SqlException(message=str(exc))

    async def read(self, product_id: int, session: AsyncSession):
        result = await session.execute(select(ProductModel).where(ProductModel.id == product_id))
        order = result.scalar_one_or_none()
        return ProductSchema.model_validate(order)

    async def read_all(self, session: AsyncSession) -> list[ProductSchema]:
        result = await session.execute(select(ProductModel))
        products = result.scalars().all()
        return [ProductSchema.model_validate(product) for product in products]

    async def update(self, obj_id: int, data: dict, session: AsyncSession) -> None:
        pass

    async def delete(self, obj_id: int, session: AsyncSession) -> None:
        pass


product_crud = ProductCRUD()