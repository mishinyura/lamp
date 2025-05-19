from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.orders import order_router

ROUTES = {
    '': order_router
}


def set_routes(app: FastAPI):
    """Устанавливает в приложение ручки"""
    for prefix, router in ROUTES.items():
        app.include_router(router=router, prefix=prefix)


def get_app():
    """Создает приложение и возвращает уже настроенный экземпляр"""
    app = FastAPI(title='Lamp')
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://127.0.0.1:5500", "http://localhost:8000"],
        allow_credentials=True,
        allow_methods=["*"],  # Разрешить все методы (GET, POST и т.д.)
        allow_headers=["*"],  # Разрешить все заголовки
    )
    set_routes(app)
    return app