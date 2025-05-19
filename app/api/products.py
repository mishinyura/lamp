from fastapi import APIRouter
from fastapi.responses import JSONResponse
import json

product_router = APIRouter()


@product_router.get('/')
def product_list():
    return JSONResponse(status_code=200, content=json.dumps({"message": "ok"}))


@product_router.get('/{product_id}/check')
def product_list(product_id: str):
    return True


@product_router.get('/{product_id}')
def product(product_id: int):
    return product_id