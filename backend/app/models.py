from sqlalchemy import (
    DateTime,
    Column,
    ForeignKey,
    Integer,
    String,
    text)
from sqlalchemy.orm import relationship
from .database import Base, engine
# from sqlalchemy.ext.declarative import declarative_base

# from dotenv import load_dotenv
# load_dotenv(dotenv_path=".env")

# Base = declarative_base()
# metadata = Base.metadata


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, server_default=text("now()"))


class Driver(Base):
    __tablename__ = 'driver'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    phone_number = Column(Integer)
    email = Column(String)
    username = Column(String)
    password = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, server_default=text("now()"))


class Question(Base):
    __tablename__ = 'question'

    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String)
    frequency_check = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, server_default=text("now()"))


class Signature(Base):
    __tablename__ = 'signature'

    id = Column(Integer, primary_key=True, autoincrement=True)
    signature = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, server_default=text("now()"))


class CategoryQuestion(Base):
    __tablename__ = 'category_question'

    id = Column(Integer, primary_key=True)
    category = Column(ForeignKey('category.id'))
    question = Column(ForeignKey('question.id'))

    category1 = relationship('Category')
    question1 = relationship('Question')


class Vehicle(Base):
    __tablename__ = 'vehicle'

    id = Column(Integer, primary_key=True, autoincrement=True)
    make = Column(String)
    num_of_doors = Column(Integer)
    horsepower = Column(Integer)
    image_url = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, server_default=text("now()"))
    category = Column(ForeignKey('category.id'))

    category1 = relationship('Category')


class CheckLog(Base):
    __tablename__ = 'check_log'

    id = Column(Integer, primary_key=True, autoincrement=True)
    #comment = Column(String)
    #created_at = Column(DateTime)
    #updated_at = Column(DateTime, server_default=text("now()"))
    driver = Column(ForeignKey('driver.id'))
    vehicle = Column(ForeignKey('vehicle.id'))
    signature = Column(ForeignKey('signature.id'))

    driver1 = relationship('Driver')
    signature1 = relationship('Signature')
    vehicle1 = relationship('Vehicle')


class Answer(Base):
    __tablename__ = 'answer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    short_answer = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, server_default=text("now()"))
    comment = Column(String)
    photo_url = Column(String)
    question = Column(Integer)
    check_log = Column(ForeignKey('check_log.id'))

    check_log1 = relationship('CheckLog')


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    password = Column(String)
    #mail = Column(String)
    role = Column(String)


# Base.metadata.create_all(engine)
