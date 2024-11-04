from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from tortoise.contrib.fastapi import register_tortoise
from models import User, user_pydantic, user_pydanticIn
from pydantic import BaseModel
from authentication import get_hashed_password
#signals
from tortoise.signals import post_save
from typing import List,Optional,Type
from tortoise import BaseDBAsyncClient

app = FastAPI()

@post_save(User)
async def create_business(
        sender:"Type[User]",
        instance: User,
        created:bool,
        using_db: "Optional[BaseDBAsyncClient]"
):
    pass


@app.post("/registration", response_model=user_pydantic)  # Use Pydantic schema here
async def user_registration(user: user_pydanticIn):
    user_info = user.dict(exclude_unset=True)
    user_info["password"] = get_hashed_password(user_info["password"])
    user_obj = await User.create(**user_info)
    new_user = await user_pydantic.from_tortoise_orm(user_obj)
    return new_user


@app.get("/")
def index():
    return {"Message": "Hello"}


# Register Tortoise ORM
register_tortoise(
    app,
    db_url="sqlite://database.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True
)
