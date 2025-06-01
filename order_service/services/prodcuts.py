from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from order_service.database import product_crud
from order_service.schemas import ProductSchema, ProductCreateSchema, ProductAddCartSchema
from order_service.models import ProductModel
from order_service.core.exceptions import SqlException, DuplicateException, NotFoundException


class ProductService:
    def __init__(self):
        self.crud = product_crud

    async def get_product(self, product_id: int, session: AsyncSession) -> ProductSchema:
        try:
            product = await self.crud.read(product_id, session)
        except SqlException:
            raise NotFoundException(message='Product not found')
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
        except SqlException:
            raise DuplicateException(message='Product already exist')

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

        print(product.stock, product_data.amount)

        if product:
            if product.stock >= product_data.amount:
                return True
        else:
            return False

    async def update_product_data(
            self, product_id: int, product_data: ProductCreateSchema, session: AsyncSession
    ) -> None:
        product = await self.crud.read(product_id=product_id, session=session)
        if product:
            await self.crud.update(product_id=product_id, new_data=product_data, session=session)
        else:
            raise NotFoundException(message='Product not found')

    async def remove_product_from_store(self, product_id: int, session: AsyncSession) -> None:
        try:
            await self.crud.delete(product_id=product_id, session=session)
        except SqlException:
            raise NotFoundException(message='Product not found')


product_service = ProductService()