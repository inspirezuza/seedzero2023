from fastapi import FastAPI
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie, Document
from datetime import datetime

app = FastAPI()


class ToDoListDoc(Document):
    name: str
    status: str
    dateCreated: datetime = datetime.now()


class ToDoList(BaseModel):
    name: str
    status: str
    dateCreated: datetime = datetime.now()


@app.on_event("startup")
async def fastapi_start():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(client.breakfast, document_models=[ToDoListDoc])


@app.post("/todolist")
async def create_profile(task: ToDoList) -> ToDoListDoc:
    doc = ToDoListDoc(name=task.name, status=task.status)

    await doc.insert()
    return doc


@app.get("/todolist")
async def get_profiles():
    docs = await ToDoListDoc.find().to_list()
    return docs


@app.get("/todolist/{id}")
async def get_profiles(id: str):
    docs = await ToDoListDoc.find().to_list()
    return docs


# @app.get("/profiles/{id}")
# async def get_profile(id: str):
#     doc = await ProfileDoc.get(id)
#     return doc


# @app.delete("/profiles/{id}")
# async def delete_profile(id: str):
#     doc = await ProfileDoc.get(id)
#     await doc.delete()
#     return doc


# @app.put("/profiles/{id}")
# async def replace_profile(id: str, task: Profile):
#     doc = await ProfileDoc.get(id)
#     doc.name = task.name
#     doc.surname = task.surname
#     await doc.save()
#     return doc
