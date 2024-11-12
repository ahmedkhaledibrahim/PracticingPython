from fastapi.params import Path
from passlib.context import CryptContext
from fastapi import Depends,FastAPI,HTTPException
from sqlalchemy.orm import Session
from typing import Union
from sql_app_package.database import SessionLocal, engine
from sql_app_package import crud, schemas, models
from sql_app_package.models import User
from sql_app_package.schemas import UserCreate


pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.post("/users/add/", response_model=schemas.User, status_code=201)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=401,detail="Email already exists")
    new_user = crud.create_user(db, user)
    return new_user

@app.get("/users/", response_model=list[schemas.User])
async def get_users(skip:int = 0, limit:int = 100,db: Session = Depends(get_db)):
    users_list = crud.get_users(db, skip, limit)
    return users_list

@app.get("/users/passwords", response_model=list[schemas.UserPassword])
async def get_users(skip:int = 0, limit:int = 100,db: Session = Depends(get_db)):
    users_list = crud.get_users_passwords(db, skip, limit)
    return users_list


@app.get("/users/{user_id}",response_model=schemas.User)
async def get_user(user_id:int = Path(...,gt=0),db: Session = Depends(get_db)):
    user = crud.get_user(db,user_id)
    if user is None:
        raise HTTPException(
            status_code=400,
            detail="No user found"
        )
    return user