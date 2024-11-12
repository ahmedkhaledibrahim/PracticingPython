from passlib.context import CryptContext
from sqlalchemy.orm import Session
from sql_app_package import models, schemas



pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def get_user(db:Session,user_id:int):
    return db.query(models.User).filter(user_id == models.User.id).first()

def get_user_by_email(db:Session, email:str):
    return db.query(models.User).filter(email == models.User.email).first()

def get_users(db:Session,skip:int = 0,limit:int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_users_passwords(db:Session,skip:int = 0,limit:int = 100):
    return db.query(models.User.hashed_password,models.User.email).offset(skip).limit(limit).all()

def create_user(db:Session, user: schemas.UserCreate):
    fake_hash_password = pwd_context.hash(user.password)
    db_user = models.User(
        email= user.email,
        hashed_password = fake_hash_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_items(db:Session,skip:int = 0,limit:int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db:Session, item: schemas.ItemCreate, user_id : int):
     db_item = models.Item(**item.dict(), owner_id = user_id)
     db.add(db_item)
     db.commit()
     db.refresh(db_item)