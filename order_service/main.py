import uvicorn

from order_service.core.config import settings
from order_service.core.app import get_app


if __name__ == '__main__':
    app = get_app()

    uvicorn.run(app, host=settings.app.app_host, port=settings.app.app_port)