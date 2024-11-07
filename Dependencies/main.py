from fastapi import FastAPI, Depends, Path, Query

class Person:
    name:str
    age:int
    def __init__(self,name,age:int):
        self.name = name
        self.age = age

    def increment(self):
        self.age +=1


app = FastAPI()

ahmed = Person(name="Ahmed",age=24)

async def pagination_functionality(q:str | None = None, start:int = 0, limit:int = 0):
    return {"q":q,"start":start,"limit":limit}


@app.get("/users")
async def get_users(pagination:dict = Depends(pagination_functionality)):
    return pagination


## class dependencies

@app.get("/users-class-dependency")
async def get_users_class_dependency(person:Person = Depends(lambda:ahmed)):
    ahmed.increment()
    return person.__dict__


@app.get("/user/{user_id}")
async def get_user(user_id: int = Path(..., description="The ID of the user"), q: str = Query(...)):
    return {"user_id": user_id, "q": q}