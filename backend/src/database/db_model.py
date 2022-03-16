import passlib.hash as _hash
import sqlalchemy as sql
import sqlalchemy.orm as _orm

from src.database import db_connect


class Users(db_connect.Base):
    __tablename__: str = "users"
    user_id = sql.Column(sql.Integer, primary_key=True, index=True)
    email = sql.Column(sql.String, unique=True, nullable=False)
    phone = sql.Column(sql.String, unique=True, nullable=False)
    name = sql.Column(sql.String, nullable=False)
    surname = sql.Column(sql.String)
    password = sql.Column(sql.String, nullable=False)
    discount = sql.Column(sql.Integer)
    role_id = sql.Column(sql.Integer, sql.ForeignKey('roles.role_id'), nullable=False)
    role = _orm.relationship('Roles')

    def verify_password(self, pwd: str):
        return _hash.bcrypt.verify(pwd, self.password)


class Roles(db_connect.Base):
    __tablename__: str = "roles"
    role_id = sql.Column(sql.Integer, primary_key=True, index=True)
    name = sql.Column(sql.String, nullable=False)


class Basket(db_connect.Base):
    __tablename__: str = "basket"
    basket_id = sql.Column(sql.Integer, primary_key=True, index=True)
    user_id = sql.Column(sql.Integer, sql.ForeignKey('users.user_id'))
    user = _orm.relationship("Users")


class Products(db_connect.Base):
    __tablename__: str = "products"
    product_id = sql.Column(sql.Integer, primary_key=True, index=True)
    name = sql.Column(sql.String, nullable=False)
    description = sql.Column(sql.String, nullable=False)
    price = sql.Column(sql.Integer, nullable=False)
    category = sql.Column(sql.Text, nullable=False)


class Sizes(db_connect.Base):
    __tablename__: str = "sizes"
    size_id = sql.Column(sql.Integer, primary_key=True)
    size = sql.Column(sql.Float, nullable=False)
    product_id = sql.Column(sql.Integer, sql.ForeignKey('products.product_id'))
    product = _orm.relationship("Products")


class Images(db_connect.Base):
    __tablename__: str = "images"
    img_id = sql.Column(sql.Integer, primary_key=True, index=True)
    url = sql.Column(sql.String)
    product_id = sql.Column(sql.Integer, sql.ForeignKey("products.product_id"))
    product = _orm.relationship('Products', innerjoin=True)


class BasketProducts(db_connect.Base):
    __tablename__: str = "basketproducts"
    basket_products_id = sql.Column(sql.Integer, primary_key=True, index=True)
    basket_id = sql.Column(sql.Integer, sql.ForeignKey('basket.basket_id'))
    basket = _orm.relationship("Basket")
    product_id = sql.Column(sql.Integer, sql.ForeignKey('products.product_id'))
    product = _orm.relationship("Products")


class Reviews(db_connect.Base):
    __tablename__: str = "reviews"
    review_id = sql.Column(sql.Integer, primary_key=True, index=True)
    text_review = sql.Column(sql.String)
    rating = sql.Column(sql.Integer)
    user_id = sql.Column(sql.Integer, sql.ForeignKey('users.user_id'))
    user = _orm.relationship("Users")
    product_id = sql.Column(sql.Integer, sql.ForeignKey('products.product_id'))
    product = _orm.relationship('Products')
