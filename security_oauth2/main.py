from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel


fake_users_db = {
    "ahmed": dict(
        username = "ahmed",
        full_name = "ahmed khaled",
        email = "ahmed.khaled@gmail.com",
        hashed_password = "fakehashedsecret",
        disabled=False
    ),
    "khaled": dict(
        username = "khaled",
        full_name = "khaled ibrahim",
        email = "khaled@gmail.com",
        hashed_password = "fakehashedsecret2",
        disabled=False
    )
}

def fake_hash_password(password:str):
    return f"fakehashed{password}"

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")
app = FastAPI()

class User(BaseModel):
    username:str
    email: str | None = None
    full_name: str | None = None
    disabled:bool | None = None

class UserInDB(User):
    hashed_password:str

def get_user(db,username:str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    return get_user(fake_users_db,token)

async def get_current_user(token:str = Depends(oauth_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials"
        )
    return user


async def get_current_active_user(current:User = Depends(get_current_user)):
    if current.disabled:
        raise HTTPException(
            status_code=401,
            detail="Inactive user"
        )
    return current

@app.get("/users/me")
async def get_me(current_user:User = Depends(get_current_active_user)):
    return current_user

@app.get("/items")
async def read_items(token: str = Depends(oauth_scheme)):
    return {"token":token}

@app.post("/token")
async def login(form_data:OAuth2PasswordRequestForm=Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password"
        )
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password"
        )
    return {"access_token":user.username,"token_type":"bearer"}