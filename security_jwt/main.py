from datetime import timedelta, datetime

from fastapi import FastAPI, Depends, HTTPException
from fastapi.openapi.utils import status_code_ranges
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import jwt, JWTError
from pydantic import BaseModel
from tortoise.signals import post_save
from typing_extensions import deprecated

app = FastAPI()

SECRET_KEY = "sdfsgrergefgdfgetgrhnnbyrqqw"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    "ahmed": dict(
        username = "ahmed",
        full_name = "ahmed khaled",
        email = "ahmed.khaled@gmail.com",
        hashed_password = "$2b$12$eM.P3r3cs8mz7lHgKp5ZHuSFh00XsPdf159sIAVdIzLE7dWb2n45q",
        disabled=False
    ),
    "khaled": dict(
        username = "khaled",
        full_name = "khaled ibrahim",
        email = "khaled@gmail.com",
        hashed_password = "$2b$12$tLbUkbIeIpnaOlXgzcFYkeNngfSoZI6IXrvLGZaDvV994UJ.Vi8Qu",
        disabled=False
    )
}

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username:str
    email: str | None = None
    full_name: str | None = None
    disabled:bool | None = None

class UserInDB(User):
    hashed_password:str


pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

def get_hashed_password(password):
    return pwd_context.hash(password)

def get_user(db,username:str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(fake_db, username:str,password:str):
    user = get_user(fake_db,username)
    if not user:
        return False
    if not verify_password(password,user.hashed_password):
        return False
    return user


def create_access_token(data:dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt



@app.post("/token")
async def login_for_access_token(username:str,password:str):
    user = authenticate_user(fake_users_db,username,password)
    if not user:
        raise HTTPException(
            status_code= 401,
            details="Incorrect username or password",
            headers = {"WWW-Authenticate":"Bearer"}
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data = {"sub":user.username},expires_delta = access_token_expires)
    return {"access_token":access_token,"token_type":"bearer"}


async def get_current_user(token:str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail = "Could not validate credentials",
        headers = {"WWW-Authenticate":"Bearer"}
    )
    try:
      payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
      username:str = payload.get("sub")
      if username is None:
          raise credentials_exception
      token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db,username = token_data.username)
    if not user:
        raise credentials_exception
    return user


async def get_current_active_user(current_user:User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400,detail="Inactive User")
    return current_user

@app.get("/users/me",response_model=User)
async def get_me(current_user:User = Depends(get_current_active_user)):
    return current_user

@app.get("/products")
async def get_products(token:str = Depends(oauth2_scheme)):
    return [{
        "name":"book",
        "price":123
    }]
