from typing import List, Optional

from pydantic import BaseModel


class Vehicle(BaseModel):
    id: int
    make: str
    num_of_doors: int
    horsepower: int
    image_url: Optional[str] = None

    class Config:
        orm_mode = True


class Question(BaseModel):
    id: int
    question: str
    frequency_check: str

    class Config:
        orm_mode = True


class CheckLog(BaseModel):
    id: int
    comment: Optional[str] = None
    driver: int
    vehicle: int
    signature: Optional[int] = None

    class Config:
        orm_mode = True


class CheckLogCreate(BaseModel):
    id: int
    comment: str
    driver: int
    vehicle: int
    signature: int

    class Config:
        orm_mode = True


# class ItemBase(BaseModel):
#     title: str
#     description: Optional[str] = None


# class ItemCreate(ItemBase):
#     pass


# class Item(ItemBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True


# class UserBase(BaseModel):
#     email: str


# class UserCreate(UserBase):
#     password: str


# class User(UserBase):
#     id: int
#     is_active: bool
#     items: List[Item] = []

#     class Config:
#         orm_mode = True
