from model import *
from sqlalchemy import create_engine, Integer, String, ForeignKey, select, insert
from uuid import uuid4
from datetime import datetime, timedelta

'''
def login(db: Session, username: str, password: str):
    with db.begin():
        res = db.execute(select(Users3).where(Users3.username == username)).scalars().all()
        if (len(res) == 0):
            print("yes")
            return -1

        print("here")
        #print(res[0])
        return 0

'''

def login(db: Session, item: Item):
    with db.begin():
        res = db.execute(select(Users3).where(Users3.username == item.username).where(Users3.password == item.password)).scalars().all()
        if (len(res) == 0):
            print("incorrect login or password")
            return "-1"

        print("you are wellcome")
        #token = str(uuid4())
        print(token)
        #deadline = (datetime.now() + timedelta(days=1)).timestamp() # time when token expires
        #rd.set(token, deadline)
        return "0"
        #return token
        # return 0


def register(db: Session, item: Item):
    with db.begin():
        res = db.execute(select(Users3).where(Users3.username == item.username)).scalars().all()
        if (len(res) == 0):
            print("create new user")
            db.execute(insert(Users3).values(username=item.username, password=item.password))
            return 0

        print("this username already taken")
        return -1

def getBooks(db: Session):
    with db.begin():
        res = db.execute(select(Books3.author, Books3.bookname, Books3.genre))  # .scalars().all()
        print(res)
        return res.mappings().all()

def insertBook(tok: Token, book: Book, db: Session):
    if rd.get(tok.token) != None and datetime.now().timestamp() <= float(rd.get(tok.token)):
        with db.begin():
            db.execute(insert(Books3).values(author=book.author, bookname=book.bookname, genre=book.genre)).scalars().all()
            return 0
    return -1

def deleteBook(book: Book, db: Session):
    with db.begin():
        db.execute(delete(Books3).where(Books3.author == book.author).where(Books3.bookname == book.bookname))
        print("book was deleted")
        return 0
