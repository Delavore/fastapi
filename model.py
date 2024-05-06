from connection import *
from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, ForeignKey, select
from sqlalchemy.orm import Session, as_declarative, declared_attr, mapped_column, sessionmaker
from pydantic import BaseModel
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

class Item(BaseModel):
    username: str
    password: str


class Book(BaseModel):
    bookname: str
    author: str
    genre: str

@as_declarative()
class Model:
    id = mapped_column(Integer, primary_key=True, autoincrement=True)

    @classmethod
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

class Users3(Model):
    username = mapped_column(String, unique=True) # String(30)
    password = mapped_column(String) # String(255)
    #active = mapped_column(Boolean)
    #time = mapped_column(Integer)
    #token = mapped_column(String)

class Books3(Model):
    bookname = mapped_column(String)
    author = mapped_column(String)
    genre = mapped_column(String)

class Statistic3(Model):
    user_id = mapped_column(ForeignKey('users3.id'))
    book_id = mapped_column(ForeignKey('books3.id'))
    pages = mapped_column(Integer)

Model.metadata.create_all(engine)
