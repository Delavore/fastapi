from model import *
from sqlalchemy import create_engine, Integer, String, ForeignKey, select, insert

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
            return -1

        print("you are wellcome")
        return 0


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
        res = db.execute(select(Books3.author, Books3.bookname, Books3.genre)).scalars().all()
        print(res)
        return res
