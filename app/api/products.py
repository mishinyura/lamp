from fastapi import APIRouter, Request, Body, Depends
from fastapi.responses import JSONResponse, Response
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT, HTTP_200_OK
from sqlalchemy.ext.asyncio import AsyncSession
import json

from app.schemas import ProductSchema, ProductCreateSchema, ProductAddCartSchema
from app.core.exceptions import DuplicateException
from app.core.db import get_session
from app.services import product_service

product_router = APIRouter()


@product_router.get('/', response_model=list[ProductSchema])
async def get_product_list(session: AsyncSession = Depends(get_session)):
    products = await product_service.get_all_products(session=session)

    if not products:
        return Response(status_code=HTTP_404_NOT_FOUND)
    return products


@product_router.get('/{order_id}', response_model=ProductSchema)
async def get_product(order_id: int, session: AsyncSession = Depends(get_session)):
    product = await product_service.get_product(order_id, session)

    if not product:
        return Response(status_code=HTTP_404_NOT_FOUND)
    return product


@product_router.post('/check', response_model=bool)
async def product_availability(
        product_data: ProductAddCartSchema, session: AsyncSession = Depends(get_session)
):

    permission = await product_service.check_availability_product(
        product_data=product_data, session=session
    )

    if permission:
        return True
    else:
        return False


@product_router.post('/', response_model=None)
async def create_product(product_data: ProductCreateSchema, session: AsyncSession = Depends(get_session)):
    try:
        await product_service.create_product(product_data=product_data, session=session)
    except DuplicateException:
        return Response(status_code=HTTP_409_CONFLICT)
    return Response(status_code=HTTP_201_CREATED)