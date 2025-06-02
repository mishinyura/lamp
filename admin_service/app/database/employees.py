from abc import ABC

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from app.core.exceptions import SqlException
from app.models import EmployeeModel
from app.schemas import EmployeeSchema
from app.database.base_crud import BaseCrud


class EmployeeCRUD(BaseCrud, ABC):
    async def create(self, employee: EmployeeModel, session: AsyncSession) -> None:
        try:
            session.add(employee)
            await session.commit()
        except SQLAlchemyError as exc:
            await session.rollback()
            raise SqlException(message=str(exc))

    async def get(self, employee_id: int, session: AsyncSession):
        result = await session.execute(select(EmployeeModel).where(EmployeeModel.id == employee_id))
        employee = result.scalar_one_or_none()
        return EmployeeSchema.model_validate(employee)

    async def update(self, employee_id: int, data: dict, session: AsyncSession) -> None:
        pass

    async def delete(self, obj_id: int, session: AsyncSession) -> None:
        pass


employee_crud = EmployeeCRUD()