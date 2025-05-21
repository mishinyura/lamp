from abc import ABC

from sqlalchemy import select, update, func
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
        product = result.scalar_one_or_none()
        return ProductSchema.model_validate(product)

    async def update(self, product_id: int, data: dict, session: AsyncSession) -> bool:
        try:
            result = await session.execute(
                update(ProductModel)
                .where(ProductModel.id == product_id)
                .values(**data)
                .execution_options(synchronize_session="fetch")
            )
            await session.commit()
            return result.rowcount > 0
        except SQLAlchemyError:
            await session.rollback()
            raise


    async def delete(self, obj_id: int, session: AsyncSession) -> None:
        pass

    @classmethod
    async def get_by_article(cls, product_article: int, session: AsyncSession):
        result = await session.execute(select(ProductModel).where(ProductModel.article == product_article))
        product = result.scalar_one_or_none()
        return ProductSchema.model_validate(product)

    @classmethod
    async def read_all(cls, session: AsyncSession) -> list[ProductSchema]:
        result = await session.execute(select(ProductModel))
        products = result.scalars().all()
        return [ProductSchema.model_validate(product) for product in products]

    @classmethod
    async def get_products_in_list(cls, products: list, session: AsyncSession) -> ProductSchema:
        result = await session.execute(
            select(ProductModel).where(ProductModel.article.in_(products))
        )

        products = result.scalars().all()
        return ProductSchema.model_validate(products)


product_crud = ProductCRUD()