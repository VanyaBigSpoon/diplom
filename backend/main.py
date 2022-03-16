from fastapi import FastAPI, Depends, security, HTTPException, UploadFile, status
from sqlalchemy import orm

from src.controllers.controller_auth import controller_generate_token
from src.controllers.controller_product import controller_create_product, controller_update_product, \
    controller_delete_product, controller_get_all_products, get_current_product
from src.controllers.controller_review import controller_create_new_review, controller_get_reviews_by_product, \
    controller_delete_review_by_id
from src.controllers.controller_roles import RolesChecker
from src.controllers.controller_user import controller_create_new_user, controller_get_current_user, \
    controller_update_user, controller_delete_user
from src.controllers.controllet_basket import controller_get_products_from_basket, \
    controller_delete_product_from_basket, controller_add_product_in_basket
from src.database.db_connect import get_db
from src.scheme.scheme_product import SchemeProductCreate, SchemeProductUpdate
from src.scheme.scheme_user import SchemeUserCreate, SchemeUser, SchemeUserUpdate

app = FastAPI()

admin = RolesChecker([2])


# РЕГИСТРАЦИЯ
@app.post('/api/auth/registration', tags=["Auth"], status_code=status.HTTP_201_CREATED)
async def registration(user: SchemeUserCreate, db: orm.Session = Depends(get_db)):
    user = await controller_create_new_user(user, db)
    return user


@app.post('/api/auth/token', tags=["Auth"], status_code=status.HTTP_200_OK)
async def login(form_data: security.OAuth2PasswordRequestForm = Depends(), db: orm.Session = Depends(get_db)):
    token = await controller_generate_token(form_data, db)
    return token


# ПОЛЬЗОВАТЕЛЬ
@app.get('/api/user/{user_id}', response_model=SchemeUser, tags=["User"], status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id: int, user: SchemeUser = Depends(controller_get_current_user)):
    if user_id != user.user_id:
        raise HTTPException(status_code=401, detail="Нет доступа")
    return user


@app.get('/api/current_user/me', response_model=SchemeUser, tags=["User"], status_code=status.HTTP_200_OK)
async def get_user(user: SchemeUser = Depends(controller_get_current_user)):
    return user


@app.patch('/api/user/me', tags=["User"], status_code=status.HTTP_200_OK)
async def update_user(
        user_update: SchemeUserUpdate,
        user: SchemeUser = Depends(controller_get_current_user),
        db: orm.Session = Depends(get_db)
):
    return_user = await controller_update_user(user_update, user, db)
    return return_user


@app.delete('/api/user/me', tags=["User"], status_code=status.HTTP_200_OK)
async def delete_user(user_id: int, user: SchemeUser = Depends(controller_get_current_user),
                      db: orm.Session = Depends(get_db)):
    await controller_delete_user(user_id, user, db)


# ПРОДУКТЫ
@app.get('/api/products', tags=["Products"], status_code=status.HTTP_200_OK)
async def get_products_list(page: int, limit: int = 9, category: str = None, search: str = None, db: orm.Session = Depends(get_db)):
    product_list = await controller_get_all_products(page, limit, category, search, db)
    return product_list


@app.get('/api/products/{id}', tags=["Products"], status_code=status.HTTP_200_OK)
async def get_product(id: int, db: orm.Session = Depends(get_db)):
    product = await get_current_product(id, db)
    return product


@app.post('/api/products/{id}', tags=["Products"], status_code=status.HTTP_201_CREATED)
async def add_product_to_basket(id: int,
                                user: SchemeUser = Depends(controller_get_current_user),
                                db: orm.Session = Depends(get_db)):
    product = await controller_add_product_in_basket(user, id, db)
    return product


# АДМИН
@app.post('/api/admin/product', tags=["Admin"], status_code=status.HTTP_201_CREATED)
async def add_new_product(
        files: list[UploadFile],
        name: str,
        description: str,
        price: int,
        size: list[str],
        category: str,
        db: orm.Session = Depends(get_db),
        role_access: bool = Depends(admin),
):
    print("work")
    new_product = await controller_create_product(name, description, price, size, category, files, role_access, db)
    return new_product


@app.get('/api/admin/product', tags=["Admin"], status_code=status.HTTP_200_OK)
async def get_user(user: SchemeUser = Depends(controller_get_current_user), role_access: bool = Depends(admin)):
    if not role_access:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    return user


@app.patch('/api/admin/product/{product_id}', tags=["Admin"], status_code=status.HTTP_200_OK)
async def update_product(product: SchemeProductUpdate, product_id: int, db: orm.Session = Depends(get_db),
                         role_access: bool = Depends(admin)):
    return_product = await controller_update_product(product, product_id, db)
    return return_product


@app.delete('/api/admin/product/{product_id}', tags=["Admin"], status_code=status.HTTP_200_OK)
async def delete_product(product_id: int, db: orm.Session = Depends(get_db), role_access: bool = Depends(admin)):
    await controller_delete_product(product_id, db)


# КОРЗИНА
@app.get('/api/basket', tags=["Basket"], status_code=status.HTTP_200_OK)
async def get_basket(user: SchemeUser = Depends(controller_get_current_user),
                     db: orm.Session = Depends(get_db)):
    basket = await controller_get_products_from_basket(user, db)
    return basket


@app.delete('/api/basket/{product_id}', tags=["Basket"], status_code=status.HTTP_200_OK)
async def delete_product_from_basket(product_id: int, db: orm.Session = Depends(get_db),
                                     user: SchemeUser = Depends(controller_get_current_user)):
    await controller_delete_product_from_basket(user, product_id, db)


@app.post('/api/basket', tags=["Basket"], status_code=status.HTTP_201_CREATED)
async def buy_products_from_basket(db: orm.Session = Depends(get_db),
                                   user: SchemeUser = Depends(controller_get_current_user)):
    return {"result": "ok"}


# ОТЗЫВЫ
@app.post('/api/products/{product_id}/review', tags=["Review"], status_code=status.HTTP_201_CREATED)
async def add_new_review(
        product_id: int,
        text_review: str,
        rating: int,
        user: SchemeUser = Depends(controller_get_current_user),
        db: orm.Session = Depends(get_db)):
    new_review = await controller_create_new_review(product_id, text_review, rating, user, db)
    return new_review


@app.get('/api/products/{product_id}/review', tags=["Review"], status_code=status.HTTP_200_OK)
async def get_reviews_by_product(product_id: int, db: orm.Session = Depends(get_db)):
    products = await controller_get_reviews_by_product(product_id, db)
    return products


@app.delete('/api/products/{product_id}/review{review_id}', tags=["Review"], status_code=status.HTTP_200_OK)
async def delete_review_by_id(review_id: int, user: SchemeUser = Depends(controller_get_current_user),
                              db: orm.Session = Depends(get_db)):
    await controller_delete_review_by_id(review_id, db)
