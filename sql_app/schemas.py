from datetime import date
from typing import List, Optional
from pydantic import BaseModel
import enum


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
    driver: int
    vehicle: int
    signature: int

    class Config:
        orm_mode = True


class Answer(BaseModel):
    id: int
    short_answer: str
    comment: Optional[str] = None
    photo_url: Optional[str] = None
    question: int
    check_log: int

    class Config:
        orm_mode = True


class Role(str, enum.Enum):
    admin: str = "admin"
    personal: str = "personel"


class User(BaseModel):
    username: str
    password: str
    # ... means this parameter is compulsory
    # mail: str = Query(..., regex="[^@ \t\r\n]+@[^@ # \t\r\n]+\.[^@ \t\r\n]+")
    #disabled: bool = False
    role: Role = None

    class Config:
        orm_mode = True
