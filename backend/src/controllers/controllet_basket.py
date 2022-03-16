from fastapi import HTTPException, status
from sqlalchemy import orm

from src.scheme.scheme_user import SchemeUser
from src.services.service_basket import service_get_products_from_basket, service_add_product_in_basket, \
    service_delete_product_from_basket
from src.services.service_product import service_get_product_by_id


async def controller_get_products_from_basket(user: SchemeUser, db: orm.Session):
    data = await service_get_products_from_basket(user.user_id, db)
    return data


async def controller_add_product_in_basket(user: SchemeUser, product_id: int, db: orm.Session):
    product = await service_get_product_by_id(product_id, db)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Продукт не найден")
    new_product = await service_add_product_in_basket(product_id, user.user_id, db)
    return new_product


async def controller_delete_product_from_basket(user: SchemeUser, product_id: int, db: orm.Session):
    product = await service_get_product_by_id(product_id, db)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Продукт не найден")
    await service_delete_product_from_basket(product_id, user.user_id, db)
