from sqlalchemy.orm import Session
from typing import Union
from fastapi import FastAPI, HTTPException, Request, status, Depends
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    exist_user = crud.get_user_by_email(db, email=user.email)
    if exist_user:
        raise  HTTPException(status_code=400, detail="user exists")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        users = crud.get_users(db, skip=skip, limit = limit)
        return users
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))


# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request, exc):
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content=jsonable_encoder({ "detail": str(exc.detail)})
#     )

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content=jsonable_encoder({ "detail": exc.errors(), "body": exc.body})
#     )
    

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None

# @app.get('/')
# def read_root():
#     # http://127.0.0.1:8000/
#     return {"Hello": "World"}

# @app.get('/items/{item_id}')
# def read_item(item_id: int, q: Union[str, None] = None):
#     # http://127.0.0.1:8000/items/1?q=sdsf
#     if item_id < 0:
#         raise HTTPException(status_code=418, detail="you can not get a negative value")
    
#     return {"item_id": item_id, "q": q}

# @app.put('/items/{item_id}')
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}