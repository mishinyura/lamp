from pydantic import BaseModel, ConfigDict

from admin_app.core.enums import EmployeeRole, EmployeeStatus


class EmployeeSchema(BaseModel):
    id: int
    name: str
    username: str
    hash_password: str
    role: EmployeeRole
    status: EmployeeStatus

    model_config = ConfigDict(from_attributes=True)


class EmployeeLoginSchema:
    username: str
    password: str