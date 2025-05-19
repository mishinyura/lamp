from fastapi import APIRouter, Request, Body
from fastapi.responses import JSONResponse
import json

product_router = APIRouter()


@product_router.get('/')
def product_list():
    return JSONResponse(status_code=200, content=json.dumps({"message": "ok"}))


@product_router.post('/check')
async def product_list(request: Request):
    count = 2
    data = await request.json()
    print(data)
    if int(data['count']) >= count:
        return False
    else:
        return True


@product_router.get('/{product_id}')
def product(product_id: int):
    return product_id