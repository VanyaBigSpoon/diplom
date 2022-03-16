from fastapi import HTTPException, UploadFile, status
from sqlalchemy import orm

from src.database.db_connect import get_db
from src.scheme.scheme_product import SchemeProductCreate, SchemeProductUpdate
from src.services.service_product import service_get_product_by_name, service_add_new_product, service_delete_product, \
    service_get_product_by_id, service_update_product, service_get_all_products, service_get_products_by_category, \
    service_get_products_by_category_and_search, service_get_products_by_name


async def controller_create_product(name: str, description: str, price: int, size: list[str], category: str,
                                    files: list[UploadFile], role_access, db: orm.Session):
    if not role_access:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Операция не доступна")
    old_product = await service_get_product_by_name(name, db)
    if old_product:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Такой продукт уже существует")
    product = SchemeProductCreate(
        description=description,
        name=name,
        price=price,
        category=category
    )
    new_product = await service_add_new_product(product, files, size, db)
    return new_product


async def controller_update_product(product: SchemeProductUpdate, product_id: int, db: orm.Session):
    current_product = await service_get_product_by_id(product_id, db)
    if not current_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Продукт не найден")
    update_product = await service_update_product(product, product_id, db)
    return update_product


async def controller_delete_product(product_id: int, db: orm.Session):
    current_product = await service_get_product_by_id(product_id, db)
    if not current_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Продукт не найден")
    await service_delete_product(product_id, db)


async def controller_get_all_products(page: int, limit: int, category: str, search: str, db: orm.Session):
    pages = page * limit
    if not (category or search):
        data = await service_get_all_products(pages, limit, db)
    elif category and search:
        data = await service_get_products_by_category_and_search(pages, limit, category, search, db)
    elif search:
        data = await service_get_products_by_name(pages, limit, search, db)
    else:
        data = await service_get_products_by_category(pages, limit, category, db)
    return data


async def get_current_product(product_id: int, db: orm.Session):
    product = await service_get_product_by_id(product_id, db)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Продукт не найден")
    return product
