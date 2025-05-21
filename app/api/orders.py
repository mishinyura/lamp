from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import json

from app.schemas.orders import OrderSchema
from app.models.orders import OrderModel
from app.core.db import get_session
from app.services.orders import order_service


order_router = APIRouter()


@order_router.get('/', response_model=list[OrderSchema])
async def order_list(session: AsyncSession = Depends(get_session)):
    orders = await order_service.get_all_orders(session=session)
    return orders


@order_router.get('/{order_id}')
async def order(order_id: int, session: AsyncSession = Depends(get_session)):
    order = await order_service.get_order(order_id, session)
    return order


@order_router.post('/')
async def create_order(order_data: OrderSchema, session: AsyncSession = Depends(get_session)):
    order = {}
    return order