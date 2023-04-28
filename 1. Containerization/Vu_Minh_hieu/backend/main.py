from model import Student
from database import (
    fetch_all_students
)
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import database
from bson import ObjectId
from typing import List

# App object
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.on_event("startup")
async def import_data_from_json_to_mongodb():
    # Read data from file JSON
    with open("data.json", "r") as f:
        data = json.load(f)

    # Convert data to format of model Student
    students = [Student(**record) for record in data]

    # Connect to collection MongoDB
    collection: collection = database["student"]

    # Remove all data in collection, then add new data
    await collection.delete_many({})
    await collection.insert_many([student.dict() for student in students])


@app.get("/")
async def get_todo():
    response = await fetch_all_students()
    return response
