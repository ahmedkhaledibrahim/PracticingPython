from fastapi import FastAPI
from.app_routes import app_router
app = FastAPI()

app.include_router(app_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI app!"}