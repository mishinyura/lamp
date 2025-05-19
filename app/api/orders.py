from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import json

from app.schemas.orders import OrderSchema
from app.models.orders import OrderModel
from app.core.db import get_session


order_router = APIRouter()


@order_router.get('/', response_model=list[OrderSchema])
async def order_list(session: AsyncSession = Depends(get_session)):
    stmt = select(OrderModel)
    result = await session.execute(stmt)
    orders = result.scalars().all()
    return orders


@order_router.get('/{order_id}')
def order(order_id: int):
    return order_id