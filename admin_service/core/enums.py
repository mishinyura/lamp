from enum import Enum


class EmployeeStatus(str, Enum):
    WORK = "Работает"
    DISMISSED = "Уволен"


class EmployeeRole(str, Enum):
    ADMIN = "Администратор"
    USER = "Пользователь"