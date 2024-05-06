from crud import *
from fastapi import FastAPI, Depends

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/login")
async def loginF(item: Item, db: Session = Depends(get_db)):
    result = login(db, item)
    return result

@app.post("/register")
async def registerF(item: Item, db: Session = Depends(get_db)):
    result = register(db, item)
    return result

@app.get("/books")
async def getBooksF(db: Session = Depends(get_db)):
    result = getBooks(db)
    return result

@app.post("/insertBook")
async def insertBookF(book: Book, db: Session = Depends(get_db)):
    result = insertBook(book, db)
    return result

# ---> add privilegence for this operation <---
@app.post("/deleteBook")
async def deleteBookF(book: Book, db: Session = Depends(get_db)):
    result = deleteBook(book, db)
    return result
    
'''
@app.post("/login/")
async def read_users(db: Session = Depends(get_db), username: str = "", password: str = ""):
    result = login(db, username, password)
    return result

@app.post("/token")
async def generate(form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data)
    return {" token": form_data.username, "token_type": "Bearer"}

@app.get("/users/self")
async def myself(token: str = Depends(oauth_scheme)):
    print("here")
    return 1001
'''
