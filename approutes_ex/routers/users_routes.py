from fastapi import APIRouter

router = APIRouter()

@router.get("/users",tags=["users"])
async def get_users():
    return [{"username":"ahmed"},{"username":"khaled"},{"username":"ibrahim"}]

@router.post("/users",tags=["users"])
async def create_user(user:dict):
    return {"created user":user}