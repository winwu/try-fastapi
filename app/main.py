from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException, status, Depends
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
        raise  HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user exists")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit = limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id = user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user not found')

    # print(user.items)
    # for item in user.items:
    #     print(item.title)
    return user

@app.post("/users/{user_id}/items", response_model=schemas.Item)
def create_item_for_user(user_id: int, item: schemas.ItemCreate,  db: Session = Depends(get_db)):
    item = crud.create_user_item(db, item, user_id)
    return item


@app.get("/items", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_items(db, skip, limit)