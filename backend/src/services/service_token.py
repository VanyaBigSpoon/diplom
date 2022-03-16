import jwt as _jwt
from fastapi import security

from settings import SECRET_KEY
from src.database.db_model import Users
from src.scheme.scheme_user import SchemeUser as _SchemeUser


async def service_create_token(user: Users):
    print(user)
    current_user = _SchemeUser.from_orm(user)
    token = _jwt.encode(current_user.dict(), SECRET_KEY)
    return dict(access_token=token, token_type="bearer")


def service_auth():
    return security.OAuth2PasswordBearer(tokenUrl="/api/auth/token")
