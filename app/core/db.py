from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.models.base import Base
from app.models import users, orders, orders_products, products
from app.core.config import settings


engine = create_async_engine(
    url=settings.db.url,
    echo=True
)

async_session_maker = async_sessionmaker(
    engine=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_session():
    async with async_session_maker() as session:
        yield session


async def create_tables():
    print(settings.db.url)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)