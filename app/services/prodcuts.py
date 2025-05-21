from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.database import product_crud
from app.schemas import ProductSchema, ProductCreateSchema, ProductAddCartSchema
from app.models import ProductModel
from app.core.exceptions import SqlException, DuplicateException


class ProductService:
    def __init__(self):
        self.crud = product_crud

    async def get_product(self, product_id: int, session: AsyncSession) -> ProductSchema:
        product = await self.crud.read(product_id, session)
        return product

    async def get_all_products(self, session: AsyncSession) -> List[ProductSchema]:
        products = await self.crud.read_all(session=session)
        return products

    async def create_product(
            self, product_data: ProductCreateSchema, session: AsyncSession
    ):
        product = ProductModel(
            article=product_data.article,
            title=product_data.title,
            stock=product_data.stock,
            price=product_data.price,
            image_url=product_data.image_url
        )
        try:
            await self.crud.create(product=product, session=session)
        except SqlException as ex:
            raise DuplicateException(message=str(ex))

    async def get_sum_products(self, products: List[dict]) -> float:
        articles = {product['article']: product['amount'] for product in products}
        products = self.crud.get_products_in_list(articles.keys())

        total = sum(
            product.price * articles.get(product.article, 0)
            for product in products
        )

        return total

    async def check_availability_product(
            self, product_data: ProductAddCartSchema, session: AsyncSession
    ) -> bool:
        product = await self.crud.get_by_article(product_article=product_data.article, session=session)
        if product.stock >= product_data.amount:
            return True
        else:
            return False


product_service = ProductService()