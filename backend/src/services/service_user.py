import passlib.hash as _hash
from sqlalchemy import orm

from src.database.db_model import Users
from src.scheme.scheme_user import SchemeUserCreate, SchemeUserUpdate, SchemeUser


async def service_get_user_by_email(email: str, db: orm.Session):
    return db.query(Users).filter(Users.email == email).first()


async def service_get_user_by_id(user_id: int, db: orm.Session):
    return db.query(Users).filter(Users.user_id == user_id).first()


async def service_create_new_user(user: SchemeUserCreate, db: orm.Session):
    new_user = Users(
        email=user.email,
        name=user.name,
        surname=user.surname,
        password=_hash.bcrypt.hash(user.password),
        role_id=1,
        discount=0,
        phone=user.phone
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def service_delete_user(user_id: int, db: orm.Session):
    user = db.query(Users).filter(Users.user_id == user_id).first()
    db.delete(user)
    db.commit()


async def serivce_update_user(user: SchemeUserUpdate, user_id: int, db: orm.Session):
    user_update = db.query(Users).filter(Users.user_id == user_id).first()
    for key, value in user.dict().items():
        if value:
            setattr(user_update, key, value)
    db.commit()
    db.refresh(user_update)
    return SchemeUser.from_orm(user_update)
