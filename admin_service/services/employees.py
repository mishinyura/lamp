from sqlalchemy.ext.asyncio import AsyncSession

from admin_service.database import employee_crud
from admin_service.schemas import EmployeeSchema, EmployeeLoginSchema
from admin_service.models import EmployeeModel
from order_service.core.exceptions import SqlException, DuplicateException


class EmployeeService:
    def __init__(self):
        self.crud = employee_crud

    async def get_employee(self, employee_id: int, session: AsyncSession) -> EmployeeSchema:
        employee = await self.crud.get(employee_id, session)
        return employee


employee_service = EmployeeService()