from fastapi import APIRouter

order_router = APIRouter(prefix='/orders')


@order_router.get('/')
def order_list():
    return ['OK']


@order_router.get('/{order_id}')
def order(order_id: int):
    return order_id