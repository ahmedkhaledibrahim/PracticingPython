from fastapi import APIRouter
from .routers import items_routes,users_routes


app_router = APIRouter()

app_router.include_router(items_routes.router)
app_router.include_router(users_routes.router)