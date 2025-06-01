from sqlalchemy import String, Integer, Enum as AlchemyEnum
from sqlalchemy.orm import Mapped, mapped_column

from admin_app.models.base import BaseModel, Base
from admin_app.core.enums import EmployeeRole, EmployeeStatus


class EmployeeModel(BaseModel, Base):
    __tablename__ = 'employees'

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    username: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    hash_password: Mapped[str] = mapped_column(String(256), nullable=False)
    role: Mapped[EmployeeRole] = mapped_column(AlchemyEnum(EmployeeRole), nullable=False, default=EmployeeRole.ADMIN)
    status: Mapped[EmployeeStatus] = mapped_column(AlchemyEnum(EmployeeStatus), nullable=False, default=EmployeeStatus.WORK)