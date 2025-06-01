from fastapi import APIRouter, Request, Body, Depends, HTTPException
from fastapi.responses import JSONResponse, Response, FileResponse
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT
from sqlalchemy.ext.asyncio import AsyncSession
import os

from order_service.schemas import ProductSchema, ProductCreateSchema, ProductAddCartSchema
from order_service.core.exceptions import DuplicateException, NotFoundException
from order_service.core.db import get_session
from order_service.services import product_service

product_router = APIRouter()


@product_router.get('/', response_model=list[ProductSchema])
async def get_product_list(session: AsyncSession = Depends(get_session)):
    """Получение всех доступных товаров в магазине"""
    products = await product_service.get_all_products(session=session)
    return products


@product_router.get('/{product_id}', response_model=ProductSchema)
async def get_product(product_id: int, session: AsyncSession = Depends(get_session)):
    """Получение товара по идентификатору"""
    try:
        product = await product_service.get_product(product_id, session)
    except NotFoundException as ex:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=str(ex))
    return product


@product_router.post('/', response_class=Response)
async def create_product(product_data: ProductCreateSchema, session: AsyncSession = Depends(get_session)):
    """Добавление нового товара в магазин"""
    try:
        await product_service.create_product(product_data=product_data, session=session)
    except DuplicateException as ex:
        raise HTTPException(status_code=HTTP_409_CONFLICT, detail=str(ex))
    return Response(status_code=HTTP_201_CREATED)


@product_router.post('/check', response_model=bool)
async def product_availability(
        product_data: ProductAddCartSchema, session: AsyncSession = Depends(get_session)
):
    """Проверка наличия нужного количества товара на складе"""
    permission = await product_service.check_availability_product(
        product_data=product_data, session=session
    )

    if permission:
        return True
    else:
        return False


@product_router.post('/static/{image_path}', response_model=bool)
async def product_availability(image_path: str):
    """Возврат фотографии"""
    path = os.path.join('order_service', 'static', image_path)
    return FileResponse(path)


@product_router.put('/{product_id}', response_model=None)
async def product_edit(
        product_id: int, product_data: ProductCreateSchema, session: AsyncSession = Depends(get_session)
):
    """Замена всех параметров товара"""
    try:
        await product_service.update_product_data(product_id, product_data, session)
    except NotFoundException as ex:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=str(ex))
    return Response(status_code=HTTP_204_NO_CONTENT)


@product_router.delete('/{product_id}', response_model=None)
async def product_delete(product_id: int, session: AsyncSession = Depends(get_session)):
    """Удаление товара из магазина"""
    try:
        await product_service.remove_product_from_store(product_id, session)
    except NotFoundException as ex:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=str(ex))
    return Response(status_code=HTTP_204_NO_CONTENT)