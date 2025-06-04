from pydantic import BaseModel, ConfigDict

from app.core.enums import EmployeeRole, EmployeeStatus


class EmployeeSchema(BaseModel):
    id: int
    name: str
    username: str
    hash_password: str
    role: EmployeeRole
    status: EmployeeStatus

    model_config = ConfigDict(from_attributes=True)


class EmployeeCreateSchema(BaseModel):
    name: str
    username: str
    password: str


class EmployeeLoginSchema:
    username: str
    password: str