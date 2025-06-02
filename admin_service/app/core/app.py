from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth_router
from app.core.config import settings, static_path
from app.core.db import create_tables

ROUTES = {
    '/admin': auth_router,
}


def set_routes(app: FastAPI):
    """Устанавливает в приложение ручки"""
    for prefix, router in ROUTES.items():
        app.include_router(router=router, prefix=prefix)


def get_app():
    """Создает приложение и возвращает уже настроенный экземпляр"""
    app = FastAPI(title='Admin')
    set_routes(app)
    app.mount(settings.admin_app.app_mount, app)
    print("STATIC PATH:", static_path)
    app.mount("/static", StaticFiles(directory=static_path), name="static")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://127.0.0.1:5500", "http://localhost:8000"],
        allow_credentials=True,
        allow_methods=["*"],  # Разрешить все методы (GET, POST и т.д.)
        allow_headers=["*"],  # Разрешить все заголовки
    )

    @app.on_event("startup")
    async def startup_event():
        await create_tables()

    return app