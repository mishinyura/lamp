from fastapi import APIRouter
from fastapi.responses import JSONResponse
import json
order_router = APIRouter(prefix='/orders')


@order_router.get('/')
def order_list():
    return JSONResponse(status_code=200, content=json.dumps({"message": "ok"}))


@order_router.get('/{order_id}')
def order(order_id: int):
    return order_id