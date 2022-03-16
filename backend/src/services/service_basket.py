from sqlalchemy import orm

from src.database.db_model import Basket, BasketProducts, Products


async def service_get_products_from_basket(user_id: int, db: orm.Session):
    basket = db.query(Basket).filter(Basket.user_id == user_id).first()
    products = db.query(BasketProducts).filter(BasketProducts.basket_id == basket.basket_id).all()
    order = [db.query(Products).filter(i.product_id == Products.product_id).first() for i in products]
    return order


async def service_add_product_in_basket(product_id: int, user_id: int, db: orm.Session):
    basket = db.query(Basket).filter(Basket.user_id == user_id).first()
    new_basket_product = BasketProducts(
        basket_id=basket.basket_id,
        product_id=product_id
    )
    db.add(new_basket_product)
    db.commit()
    db.refresh(new_basket_product)
    return new_basket_product


async def service_delete_product_from_basket(product_id: int, user_id: int, db: orm.Session):
    basket = db.query(Basket).filter(Basket.user_id == user_id).first()
    basket_product = db.query(BasketProducts).filter(BasketProducts.basket_id == basket.basket_id,
                                                     BasketProducts.product_id == product_id).first()
    db.delete(basket_product)
    db.commit()


async def service_create_basket(user_id: int, db: orm.Session):
    basket = Basket(
        user_id=user_id
    )
    db.add(basket)
    db.commit()
    db.refresh(basket)
