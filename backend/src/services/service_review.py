from sqlalchemy import orm

from src.database.db_model import Reviews, Users


async def service_create_new_review(product_id: int, text_review: str, rating: int, user_id: int, db: orm.Session):
    new_product = Reviews(
        text_review=text_review,
        rating=rating,
        user_id=user_id,
        product_id=product_id,
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


async def service_get_reviews_by_product(product_id: int, db: orm.Session):
    return db.query(Reviews, Users.name).filter(Reviews.product_id == product_id).all()


async def service_delete_review_by_id(review_id: int, db: orm.Session):
    review = db.query(Reviews).filter(Reviews.review_id == review_id).first()
    db.delete(review)
    db.commit()


async def service_get_review_by_id(review_id: int, db: orm.Session):
    return db.query(Reviews).filter(Reviews.review_id == review_id).first()
