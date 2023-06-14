from fastapi import FastAPI
import uvicorn
from sqlalchemy.orm import sessionmaker
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from database import ENGINE_DATABASE
from models import Todo
app = FastAPI()
Session = sessionmaker(bind=ENGINE_DATABASE)
session_object = Session()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TodoRequest(BaseModel):
    text: str 
    is_complete: bool = False

class TodoDelete(BaseModel):
    id: int

@app.post("/create")
async def create_todo(todo : TodoRequest):
    todo = Todo(text=todo.text, is_done=todo.is_complete)
    session_object.add(todo)
    session_object.commit()
    todos_query = session_object.query(Todo)
    return todos_query.all()

@app.delete("/delete")
async def delete_todo(pk : TodoDelete):
    todo = session_object.get(Todo, pk.id)
    session_object.delete(todo)
    session_object.commit()
    todos_query = session_object.query(Todo)
    return todos_query.all()

@app.get("/")
async def get_all_todos():
    todos_query = session_object.query(Todo)
    return todos_query.all()

if __name__ == "__main__":
    config = uvicorn.Config("main:app", host="0.0.0.0", port=4000, log_level="info", reload=True)
    server = uvicorn.Server(config)
    server.run()