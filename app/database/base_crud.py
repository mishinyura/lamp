from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any


class BaseCrud(ABC):
    @abstractmethod
    async def get(self, elem) -> Any: ...

    @abstractmethod
    async def get_all(self, session) -> list[Any]: ...

    @abstractmethod
    async def add(self, batch: Any) -> None: ...