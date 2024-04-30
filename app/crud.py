from datetime import datetime, timedelta, timezone
from typing  import Union
from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext
from jose import jwt
from . import main

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

# helper
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user_by_id(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user(db: Session, username: str):
    user = get_user_by_username(db, username)
    return user

def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})

    encode_jwt = jwt.encode(to_encode, main.SECRET_KEY, algorithm=main.ALGORITHM)
    return encode_jwt

def create_user(db: Session, user: schemas.UserCreate):
    hashed_pwd = pwd_context.hash(user.password)
    db_user = models.User(email = user.email, password=hashed_pwd, username=user.username, disabled=user.disabled)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.model_dump(), owner_id = user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item