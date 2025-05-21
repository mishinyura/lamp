from abc import ABC

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from app.core.exceptions import SqlException
from app.models import UserModel
from app.schemas import UserSchema, UserCreateSchema
from app.database.base_crud import BaseCrud


class UserCRUD(BaseCrud, ABC):
    async def create(self, user: UserModel, session: AsyncSession) -> None:
        try:
            session.add(user)
            await session.commit()
        except SQLAlchemyError as exc:
            await session.rollback()
            raise SqlException(message=str(exc))

    async def read(self, user_id: int, session: AsyncSession):
        result = await session.execute(select(UserModel).where(UserModel.id == user_id))
        user = result.scalar_one_or_none()
        return UserSchema.model_validate(user)

    async def update(self, obj_id: int, data: dict, session: AsyncSession) -> None:
        pass

    async def delete(self, obj_id: int, session: AsyncSession) -> None:
        pass

    @classmethod
    async def get_by_phone(cls, user_phone: str, session: AsyncSession) -> UserSchema | None:
        result = await session.execute(select(UserModel).where(UserModel.phone == user_phone))
        user = result.scalar_one_or_none()
        return UserSchema.model_validate(user)

    @classmethod
    async def read_all(cls, session: AsyncSession) -> list[UserSchema]:
        result = await session.execute(select(UserModel))
        users = result.scalars().all()
        return [UserSchema.model_validate(user) for user in users]


user_crud = UserCRUD()