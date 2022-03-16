import jwt
from fastapi import Depends, HTTPException, status
from sqlalchemy import orm

from settings import SECRET_KEY
from src.database.db_connect import get_db
from src.scheme.scheme_user import SchemeUserCreate, SchemeUser, SchemeUserUpdate
from src.services.service_basket import service_create_basket
from src.services.service_token import service_create_token, service_auth
from src.services.service_user import service_get_user_by_email, service_create_new_user, service_get_user_by_id, \
    service_delete_user, serivce_update_user


async def controller_create_new_user(user: SchemeUserCreate, db: orm.Session = Depends(get_db)):
    old_user = await service_get_user_by_email(user.email, db)
    if old_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Пользователь с таким email уже существует")
    new_user = await service_create_new_user(user, db)
    await service_create_basket(new_user.user_id, db)
    token = await service_create_token(new_user)
    return token


async def controller_get_current_user(token: str = Depends(service_auth()), db: orm.Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user = await service_get_user_by_id(payload["user_id"], db)
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Ошибка в логине или пароле")
    return SchemeUser.from_orm(user)


async def controller_update_user(
        user_update: SchemeUserUpdate,
        user: SchemeUser,
        db: orm.Session = Depends(get_db)
):
    return await serivce_update_user(user_update, user.user_id, db)


async def controller_delete_user(user_id: int, user: SchemeUser, db: orm.Session):
    if user_id != user.user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Нет прав")
    await service_delete_user(user_id, db)
