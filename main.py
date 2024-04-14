from fastapi import FastAPI
import databases
import psycopg2
from dotenv import find_dotenv, load_dotenv
import os

# env var
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
User = os.getenv("USER")
Password = os.getenv("PASSWD")

connect = psycopg2.connect(host='postgresql-delavore.alwaysdata.net', user=User, password=Password, dbname='delavore_db')
cursor = connect.cursor()

app = FastAPI()

@app.on_event("startup")
async def startup():
    # когда приложение запускается устанавливаем соединение с БД
    #await database.connect()
    pass


@app.on_event("shutdown")
async def shutdown():
    # когда приложение останавливается разрываем соединение с БД
    #await database.disconnect()
    cursor.close()
    connect.close()


@app.get("/")
async def root():
    a = cursor.execute("SELECT * FROM users")
    #print("here")
    row = cursor.fetchone()
    #cursor.close()
    #connect.close()
    return row


@app.get("/items")
async def get_items():
    a = cursor.execute("SELECT * FROM users")
    #print("here")
    row = cursor.fetchone()
    cursor.close()
    connect.close()
    return row
