from fastapi import FastAPI, HTTPException, Query, Path, Body
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID,uuid4

app2 = FastAPI()
#
# class Task(BaseModel):
#     id:Optional[UUID] = None
#     title: str
#     description: Optional[str] = None
#     completed: bool = False
#
# tasks = []
#
#
# @app2.get("/")
# async def root():
#     return {
#         "name":"ahmed",
#         "age":15,
#         "location":"cairo"
#     }
#
#
# @app2.get("/get-user")
# async def getuser(id:int):
#     if id == 1:
#         return {
#             "name": "khaled",
#             "age": 20,
#             "location": "Alex"
#         }
#
# @app2.get("/get-message",response_model=dict)
# async def getMessage(message:str = Query(max_length=10,min_length=5,title="Enter Message")):
#     return {
#         "message" : message
#     }
#
#
# @app2.post("/create-task",response_model=Task)
# async def createTask(task:Task):
#     task.id = uuid4()
#     tasks.append(task)
#     return task
#
# @app2.get("/get-tasks",response_model=List[Task])
# async def getTasks():
#     return tasks
#
# @app2.get("/tasks/{task_id}",response_model=Task)
# async def read_task(task_id: UUID):
#     for task in tasks:
#         if task.id == task_id:
#             return task
#     raise HTTPException(status_code = 404,detail = "Task Not Found")
#
# @app2.put("/update-task/{task_id}",response_model=Task)
# async def updatetask(task_id:UUID,task_toUpdate:Task):
#     for index,task in enumerate(tasks):
#         if task.id == task_id:
#             updated_task = task.copy(update=task_toUpdate.dict(exclude_unset=True))
#             tasks[index] = updated_task
#             return updated_task
#
#     raise HTTPException(status_code=404, detail="Task Not Found")
#
# @app2.get("/get-messages")
# async def getMessages(messages:list[str]=Query(["ahmed","khaled"])):
#     return {
#         "messages": messages
#     }
#
# @app2.get("/item-validation/{item_id}")
# async def itemvalidation(*,q:str=Query(...),item_id:int = Path(...,gt=1,lt=10)):
#     return {"id":item_id,"q":q}
#


class Item(BaseModel):
    name:str
    description:str | None = None

@app2.post("/get-item-details/{item_id}/{q}")
async def getItemDetails(q:str = Path(min_length=2),item_id:int = Path(...,gt=0,le=100,title="Enter Item Id"),item:Item = Body(...)):
    results = {}
    if item_id:
        results.update({"id":item_id})
    if q:
        results.update({"q": q})
    if item:
        results.update({"item":item})
    return results

