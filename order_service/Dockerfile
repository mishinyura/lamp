FROM python:3.12-slim

RUN pip install --no-cache-dir poetry

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . /app

EXPOSE 8002

CMD ["uvicorn", "order_service.core.app:get_app", "--factory", "--host", "0.0.0.0", "--port", "8002"]