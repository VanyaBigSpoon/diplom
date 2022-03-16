from typing import Optional

import pydantic as _pydantic


class _BaseModel(_pydantic.BaseModel):
    email: Optional[str]


class SchemeUserCreate(_BaseModel):
    name: str
    surname: str
    password: str
    phone: str

    class Config:
        orm_mode = True


class SchemeUserUpdate(_BaseModel):
    name: Optional[str]
    surname: Optional[str]
    phone: Optional[str]
    discount: Optional[int]

    class Config:
        orm_mode = True


class SchemeUser(_BaseModel):
    user_id: int
    name: str
    role_id: int
    surname: str
    discount: int
    phone: str

    class Config:
        orm_mode = True
