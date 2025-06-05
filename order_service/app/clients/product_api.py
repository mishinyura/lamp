import httpx

from app.core.config import settings


class ProductAPIClient:
    BASE_URL = settings.api.product_api

    @classmethod
    async def get_product_by_article(cls, article: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{cls.BASE_URL}/products/{article}")
            response.raise_for_status()
            return response.json()

product_client = ProductAPIClient()