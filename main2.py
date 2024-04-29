from fastapi import FastAPI, Header, Depends
from typing import Annotated, Union
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm
import databases
import psycopg2
from dotenv import find_dotenv, load_dotenv
import os
import psycopg2.extras
from pydantic import BaseModel

oauth_scheme = OAuth2PasswordBearer("token")

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

#@app.get("/time/")
#async def read_items(user_agent: Annotated[Item, Header()] = None):
#    return {"User-Agent": 5} # user_agent

@app.post("/token")
async def generate(form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data)
    return {"access_token": form_data.username, "token_type": "bearer"}

@app.get("/users/self")
async def myself(token: str = Depends(oauth_scheme)):
    print("here")
    return 1001
   


@app.post("/ton")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    a = cursor.execute("SELECT * FROM test2")
    #print("here")
    print("------------")
    print(form_data.username)
    print("------------")
    row = cursor.fetchall()
    #cursor.close()
    #connect.close()
    return row
    # return {"username": form_data.username, "password": form_data.password}

@app.post("/users/me")
async def read(item: Item):
    if item.username == "dela":
        a = cursor.execute("SELECT * FROM test2")
        #print("here")
        row = cursor.fetchall()
        #cursor.close()
        #connect.close()
        return 0
    else:
        a = cursor.execute("SELECT * FROM test2")
        #print("here")
        row = cursor.fetchone()
        x = list()
        x.append(row)
        x.append(row)
        #cursor.close()
        #connect.close()
        return -1


