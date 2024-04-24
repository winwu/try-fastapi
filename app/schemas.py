from pydantic import BaseModel, EmailStr

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


class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool 
    items: list[Item] = []

    class Config:
        from_attributes = True

