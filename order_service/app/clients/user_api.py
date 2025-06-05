import httpx

from app.core.config import settings


class UserAPIClient:
    BASE_URL = settings.api.user_api

    @classmethod
    async def get_user_by_phone(cls, name: str, phone: str):
        data = {
            'name': name,
            'phone': phone
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(f"{cls.BASE_URL}/users/", json=data)
            return response.json()


user_client = UserAPIClient()