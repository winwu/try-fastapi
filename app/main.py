from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException, status, Depends, Request, Response
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

app = FastAPI(
    title="API Guide",
    description="API description",
    summary="Summary",
    version="0.0.1",
    openapi_tags=tags_metadata
)

@app.middleware('http')
async def db_session_middleware(request: Request, call_next):
    res = Response("internal server error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    try:
        request.state.db = SessionLocal()
        res = await call_next(request)
    finally:
        request.state.db.close()
    return res

# Dependency
def get_db(request: Request):
    return request.state.db

@app.post("/users/", response_model=schemas.User, tags=["users"])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    exist_user = crud.get_user_by_email(db, email=user.email)
    if exist_user:
        raise  HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user exists")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User], tags=['users'])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit = limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User, tags=['users'])
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id = user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user not found')

    # print(user.items)
    # for item in user.items:
    #     print(item.title)
    return user

@app.post("/users/{user_id}/items", response_model=schemas.Item, tags=['items'])
def create_item_for_user(user_id: int, item: schemas.ItemCreate,  db: Session = Depends(get_db)):
    item = crud.create_user_item(db, item, user_id)
    return item


@app.get("/items", response_model=list[schemas.Item], tags=['items'])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_items(db, skip, limit)