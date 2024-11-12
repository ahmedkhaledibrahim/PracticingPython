from fastapi import APIRouter

router = APIRouter()

@router.get("/items",tags=["items"])
async def get_items():
    return [{"item":"item 1"},{"item":"item 2"},{"item":"item 3"}]

@router.post("/items",tags=["items"])
async def create_items(user:dict):
    return {"created item":user}