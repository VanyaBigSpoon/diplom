import os

from fastapi import UploadFile
from sqlalchemy import orm

from settings import UPLOADED_FILES_PATH
from src.database.db_model import Products, Images, Sizes
from src.scheme.scheme_product import SchemeProductCreate, SchemeProductUpdate


async def service_get_product_by_name(product_name: str, db: orm.Session):
    return db.query(Products).filter(Products.product_name == product_name).first()


async def service_get_product_by_id(product_id: int, db: orm.Session):
    product = db.query(Products).filter(Products.product_id == product_id).first()
    images = db.query(Images).filter(Images.product_id == product_id).all()
    sizes = db.query(Sizes).filter(Sizes.product_id == product_id).all()
    return {"product" : product, "images": images, "sizes": sizes}


async def service_add_new_product(product: SchemeProductCreate, files: list[UploadFile], sizes: list[str], db: orm.Session):
    new_product = Products(
        name=product.name,
        description=product.description,
        price=product.price,
        category=product.category,
    )
    print(new_product.name)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    for file in files:
        file_name, ext = os.path.splitext(file.filename)
        new_file_name = f"{product.name.replace(' ', '')}{file_name}{ext}"
        await service_save_file(file, new_file_name)
        await service_add_file_to_db(new_product.product_id, new_file_name, db)
    await service_add_sizes_for_product(new_product.product_id, sizes, db)
    return new_product


async def service_delete_product(product_id: int, db: orm.Session):
    current_product = db.query(Products).filter(Products.product_id == product_id).first()
    db.delete(current_product)
    db.commit()


async def service_update_product(product_id: int, product: SchemeProductUpdate, db: orm.Session):
    current_product = db.query(Products).filter(Products.product_id == product_id).first()
    current_product.price = product.price
    db.commit()
    return current_product


async def service_save_file(file, filename):
    with open(f"{UPLOADED_FILES_PATH}{filename}", "wb") as upload_file:
        file_obj = await file.read()
        upload_file.write(file_obj)
        upload_file.close()


async def service_add_file_to_db(product_id: int, file_path: str, db: orm.Session):
    new_img = Images(
        url=f"/uploaded_files//{file_path}",
        product_id=product_id,
    )
    db.add(new_img),
    db.commit()
    db.refresh(new_img)


async def service_add_sizes_for_product(product_id: int, sizes: list[str], db: orm.Session):
    sizes=sizes[0].split(',')
    for s in sizes:
        new_size = Sizes(
            size=float(s),
            product_id=product_id
        )
        db.add(new_size)
        db.commit()
        db.refresh(new_size)


async def service_get_all_products(page: int, limit: int, db: orm.Session):
    data = db.query(Products, Images.url).filter(Products.product_id == Images.product_id)
    products = data.distinct(Products.product_id).offset(page).limit(limit).all()
    value = int(len(products) / limit) + 1
    return {"products": products, "value": value, "page": page}


async def service_get_products_by_category(page: int, limit: int, category: str, db: orm.Session):
    data = db.query(Products, Images.url).filter(Products.product_id == Images.product_id, Products.category == category)
    products = data.distinct(Products.product_id).offset(page).limit(limit).all()
    value = int(len(products) / limit) + 1
    return {"products": products, "value": value, "page": page}


async def service_get_products_by_category_and_search(page: int, limit: int, category: str, search: str, db: orm.Session):
    data = db.query(Products, Images.url).filter(
        Products.product_id == Images.product_id,
        Products.category == category,
        Products.name == search
    )
    products = data.distinct(Products.product_id).offset(page).limit(limit).all()
    value = int(len(products) / limit) + 1
    return {"products": products, "value": value, "page": page}


async def service_get_products_by_name(page: int, limit: int, search: str, db: orm.Session):
    data = db.query(Products, Images.url).filter(
        Products.product_id == Images.product_id,
        Products.name == search
    )
    products = data.distinct(Products.product_id).offset(page).limit(limit).all()
    value = int(len(products) / limit) + 1
    return {"products": products, "value": value, "page": page}
