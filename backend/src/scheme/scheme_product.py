import pydantic as _pydantic


class _BaseModel(_pydantic.BaseModel):
    name: str


class SchemeProductCreate(_BaseModel):
    description: str
    price: int
    category: str

    class Config:
        orm_mode = True


class SchemeProductUpdate(_BaseModel):
    price: int

    class Config:
        orm_mode = True


class SchemeProduct(_BaseModel):
    product_id: int
    description: str
    price: int
    category: str

    class Config:
        orm_mode = True