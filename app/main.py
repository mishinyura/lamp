import uvicorn

from app.core.config import settings
from app.core.app import get_app


if __name__ == '__main__':
    app = get_app()

    uvicorn.run(app, host=settings.app.app_host, port=settings.app.app_port)