from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_409_CONFLICT, HTTP_201_CREATED, HTTP_404_NOT_FOUND

from order_service.schemas.orders import OrderSchema, OrderCreateSchema
from order_service.core.db import get_session
from order_service.services.orders import order_service
from order_service.core.exceptions import DuplicateException

order_router = APIRouter()


@order_router.get('/', response_model=list[OrderSchema])
async def get_order_list(session: AsyncSession = Depends(get_session)):
    orders = await order_service.get_all_orders(session=session)

    if not orders:
        return Response(status_code=HTTP_404_NOT_FOUND)
    return orders


@order_router.get('/{order_id}')
async def get_order(order_id: int, session: AsyncSession = Depends(get_session)):
    order = await order_service.get_order(order_id, session)

    if not order:
        return Response(status_code=HTTP_404_NOT_FOUND)
    return order


@order_router.post('/')
async def create_order(order_data: OrderCreateSchema, session: AsyncSession = Depends(get_session)):
    try:
        await order_service.create_order(order_data=order_data, session=session)
    except DuplicateException:
        return Response(status_code=HTTP_409_CONFLICT)
    return Response(status_code=HTTP_201_CREATED)
