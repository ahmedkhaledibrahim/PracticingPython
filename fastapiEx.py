from http.client import HTTPException

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID,uuid4

app = FastAPI()

class Task(BaseModel):
    id:Optional[UUID] = None
    title: str
    description: Optional[str] = None
    completed: bool = False

tasks = []


@app.get("/")
async def root():
    return {
        "name":"ahmed",
        "age":15,
        "location":"cairo"
    }


@app.get("/get-user")
async def getuser(id:int):
    if id == 1:
        return {
            "name": "khaled",
            "age": 20,
            "location": "Alex"
        }


@app.post("/create-task",response_model=Task)
async def createTask(task:Task):
    task.id = uuid4()
    tasks.append(task)
    return task

@app.get("/get-tasks",response_model=List[Task])
async def getTasks():
    return tasks

@app.get("/tasks/{task_id}",response_model=Task)
async def read_task(task_id: UUID):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code = 404,detail = "Task Not Found")