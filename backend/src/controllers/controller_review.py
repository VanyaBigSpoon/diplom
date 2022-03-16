from fastapi import HTTPException, status
from sqlalchemy import orm

from src.scheme.scheme_user import SchemeUser
from src.services.service_product import service_get_product_by_id
from src.services.service_review import service_create_new_review, service_get_reviews_by_product, \
    service_delete_review_by_id, service_get_review_by_id


async def controller_create_new_review(product_id: int, text_review: str, rating: int, user: SchemeUser,
                                       db: orm.Session):
    product = await service_get_product_by_id(product_id, db)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Продукт не найден")
    new_review = await service_create_new_review(product_id, text_review, rating, user.user_id, db)
    return new_review


async def controller_get_reviews_by_product(product_id: int, db: orm.Session):
    product = await service_get_product_by_id(product_id, db)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Продукт не найден")
    products = await service_get_reviews_by_product(product_id, db)
    return products


async def controller_delete_review_by_id(review_id, db):
    review = await service_get_review_by_id(review_id, db)
    if not review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Отзыв не найден")
    await service_delete_review_by_id(review_id, db)
