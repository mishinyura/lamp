from sqlalchemy.ext.asyncio import AsyncSession

from app.database import employee_crud
from app.schemas import EmployeeSchema


class EmployeeService:
    def __init__(self):
        self.crud = employee_crud

    async def get_employee(self, employee_id: int, session: AsyncSession) -> EmployeeSchema:
        employee = await self.crud.get(employee_id, session)
        return employee


employee_srv = EmployeeService()