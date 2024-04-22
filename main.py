from fastapi import FastAPI, Header
from typing import Annotated, Union
import databases
import psycopg2
from dotenv import find_dotenv, load_dotenv
import os
import psycopg2.extras
from pydantic import BaseModel

class Item(BaseModel):
    username: str
    password: str
    #price: float
    #tax: Union[float, None] = None


# env var
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
User = os.getenv("USER")
Password = os.getenv("PASSWD")

connect = psycopg2.connect(host='postgresql-delavore.alwaysdata.net', user=User, password=Password, dbname='delavore_db')
cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

app = FastAPI()

@app.on_event("startup")
async def startup():
    # когда приложение запускается устанавливаем соединение с БД
    #await database.connect()
    pass

'''
@app.on_event("shutdown")
async def shutdown():
    # когда приложение останавливается разрываем соединение с БД
    #await database.disconnect()
    cursor.close()
    connect.close()
'''

@app.get("/")
async def root():
    a = cursor.execute("SELECT * FROM test2")
    #print("here")
    row = cursor.fetchall()
    #cursor.close()
    #connect.close()
    return row


@app.get("/items")
async def get_items():
    a = cursor.execute("SELECT * FROM test2")
    #print("here")
    row = cursor.fetchall()
    #cursor.close()
    #connect.close()
    return row

@app.get("/time/")
async def read_items(user_agent: Annotated[Item, Header()] = None):
    return {"User-Agent": 5} # user_agent

@app.post("/users/me")
async def read(item: Item):
    if item.username == "dela":
        a = cursor.execute("SELECT * FROM test2")
        #print("here")
        row = cursor.fetchall()
        #cursor.close()
        #connect.close()
        return row
    else:
        a = cursor.execute("SELECT * FROM test2")
        #print("here")
        row = cursor.fetchone()
        x = list()
        x.append(row)
        x.append(row)
        #cursor.close()
        #connect.close()
        return x
