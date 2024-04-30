from typing import Union
from pydantic import BaseModel, EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None

class ItemBase(BaseModel):
    title: str
    description: str | None = None

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

class ItemCreate(ItemBase):
    pass


class UserCreate(BaseModel):
    password: str
    username: str
    email: Union[EmailStr | None] = None
    disabled: Union[bool, None] = None

class User(UserCreate):
    id: int
    items: list[Item] = []

    class Config:
        from_attributes = True