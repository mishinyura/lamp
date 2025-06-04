from datetime import timedelta

from sqlalchemy.ext.asyncio import AsyncSession

from app.database import employee_crud
from app.schemas import EmployeeSchema, EmployeeCreateSchema
from app.models import EmployeeModel
from app.core.security import pwd_context, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from app.core.enums import EmployeeRole, EmployeeStatus
from app.core.exceptions import DuplicateException, SqlException, NotFoundException


class EmployeeService:
    def __init__(self):
        self.crud = employee_crud

    async def get_employee(self, username: str, session: AsyncSession) -> EmployeeSchema:
        try:
            employee = await self.crud.get(username=username, session=session)
            return employee
        except SqlException:
            raise NotFoundException(message='Пользователь не найден')

    async def create_new_employee(self, data, session: AsyncSession) -> dict:
        model = EmployeeModel(
            name=data.name,
            username=data.username,
            hash_password=pwd_context.hash(data.password),
            role=EmployeeRole.ADMIN,
            status=EmployeeStatus.WORK
        )
        try:
            await self.crud.create(employee=model, session=session)
            token = create_access_token(
                data={"sub": model.username},
                expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            )
            return {'access_token': token}
        except SqlException:
            raise DuplicateException(message='Такой пользователь уже существует')


employee_srv = EmployeeService()