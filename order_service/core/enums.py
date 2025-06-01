from enum import Enum


class OrderStatus(str, Enum):
    PENDING = "В работе"
    COMPLETED = "Выполнен"
    CANCELLED = "Отменен"