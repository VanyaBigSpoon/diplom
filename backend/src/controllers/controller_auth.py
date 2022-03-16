from fastapi import Depends, HTTPException, security, status
from sqlalchemy import orm

from src.database.db_connect import get_db
from src.services.service_token import service_create_token
from src.services.service_user import service_get_user_by_email


async def controller_generate_token(form_data: security.OAuth2PasswordRequestForm = Depends(),
                                    db: orm.Session = Depends(get_db)):
    user = await controller_auth_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Данные неверны")
    token = await service_create_token(user)
    return token


async def controller_auth_user(email: str, password: str, db: orm.Session):
    user = await service_get_user_by_email(email, db)
    if not user:
        return None
    if not user.verify_password(password):
        return None
    return user
