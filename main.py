from fastapi import FastAPI
import databases
import psycopg2

connect = psycopg2.connect(host='postgresql-delavore.alwaysdata.net', user='user', password='passwd', dbname='delavore_db')
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
