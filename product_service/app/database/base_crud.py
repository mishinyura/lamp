from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any


class BaseCrud(ABC):
    @abstractmethod
    async def create(self, obj: Any, session: AsyncSession) -> None: ...

    @abstractmethod
    async def read(self, obj_id: int, session: AsyncSession) -> Any: ...

    @abstractmethod
    async def update(self, obj_id: int, data: dict, session: AsyncSession) -> None: ...

    @abstractmethod
    async def delete(self, obj_id: int, session: AsyncSession) -> None: ...
