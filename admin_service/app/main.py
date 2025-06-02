import uvicorn

from app.core.app import settings
from app.core.app import get_app


if __name__ == '__main__':
    app = get_app()

    uvicorn.run(app, host=settings.admin_app.app_host, port=settings.admin_app.app_port)