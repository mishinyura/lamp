from sqlalchemy import inspect
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from admin_app.models.base import Base
from admin_app.models import employees
from admin_app.core.config import settings


engine = create_async_engine(
    url=settings.db.url,
    echo=True
)

async_session_maker = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_session():
    async with async_session_maker() as session:
        yield session


async def create_tables():
    print(settings.db.url)
    async with engine.begin() as conn:
        inspector = await conn.run_sync(lambda conn: inspect(conn))

        existing_tables = await conn.run_sync(lambda _: inspector.get_table_names())

        # Проверяем нужные таблицы
        needed_tables = Base.metadata.tables.keys()

        tables_to_create = [table for table in needed_tables if table not in existing_tables]

        if tables_to_create:
            await conn.run_sync(
                lambda conn: Base.metadata.create_all(
                    conn,
                    tables=[Base.metadata.tables[table] for table in tables_to_create]
                )
            )
            print(f"Created tables: {tables_to_create}")
        else:
            print("All tables already exist")