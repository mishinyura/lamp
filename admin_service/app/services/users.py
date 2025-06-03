from sqlalchemy.ext.asyncio import AsyncSession

from app.database import user_crud
from app.schemas import UserSchema, UserCreateSchema
from app.models import UserModel
from app.core.exceptions import SqlException, DuplicateException


class UserService:
    def __init__(self):
        self.crud = user_crud

    async def get_user(self, user_id: int, session: AsyncSession) -> UserSchema:
        user = await self.crud.read(user_id, session)
        return user

    async def get_user_by_user_phone(self, user_phone: str, session: AsyncSession) -> UserSchema:
        user = await self.crud.get_by_phone(user_phone, session)
        return user

    async def get_all_users(self, session: AsyncSession) -> list[UserSchema]:
        users = await self.crud.read_all(session=session)
        return users

    async def create_user(
            self, user_data: UserCreateSchema, session: AsyncSession
    ) -> int:
        user = UserModel(
            name=user_data.name,
            phone=user_data.phone
        )
        try:
            await self.crud.create(user=user, session=session)
            return user.id
        except SqlException as ex:
            raise DuplicateException(message=str(ex))


user_srv = UserService()