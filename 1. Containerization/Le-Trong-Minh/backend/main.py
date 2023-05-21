from model import (
    Student,
    UpdateStudent,
    ResponseModel,
    ErrorResponseModel,
)
from database import (
    fetch_all_students,
    fetch_one_student,
    create_student,
    update_student,
    remove_student,
)
import json
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from database import database
from bson import ObjectId
from typing import List

from fastapi.encoders import jsonable_encoder
import logging
import logstash
import sys

host = '172.17.0.1'

test_logger = logging.getLogger('api-logstash')
test_logger.setLevel(logging.INFO)
# test_logger.addHandler(logstash.LogstashHandler(host, 5454, version=1))
test_logger.addHandler(logstash.TCPLogstashHandler(host, 5044, version=1))

# App object
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def import_data_from_json_to_mongodb():
    test_logger.info("Start up application", extra={"status":"ok"})
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

async def read_root():
    test_logger.info("Get api", extra={"status":"ok"})
    return {"message": "Welcome to this fantastic app!"}


@app.get("/api/v1/students")
async def get_all_students():
    test_logger.info("Get all students", extra={"status":"ok"})
    response = await fetch_all_students()
    if response:
        return ResponseModel(response, "Students data retrieved successfully")
    return ResponseModel(response, "Empty list returned")


@app.get("/api/v1/students/{id}")
async def get_student_by_id(id):
    test_logger.info("Get student information", extra={"status":"ok"})
    response = await fetch_one_student(id)
    if response:
        return ResponseModel(response, "Student data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Student doesn't exist.")


@app.post("/api/v1/students")
async def post_student(data: Student = Body(...)):
    test_logger.info("Post information", extra={"status":"ok"})
    data = jsonable_encoder(data)
    response = await create_student(data)
    if response:
        return ResponseModel(response, "Student added successfully.")
    return ErrorResponseModel("An error occurred.", 400, "Bad request.")


@app.put("/api/v1/students/{id}")
async def put_student(id: str, req: UpdateStudent = Body(...)):
    test_logger.info("Update", extra={"status":"ok"})
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_student = await update_student(id, req)
    if updated_student:
        return ResponseModel(
            "Student with ID: {} name update is successful".format(id),
            "Student name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )


@app.delete("/api/v1/students/{id}")
async def delete_student_by_id(id: str):
    test_logger.info("Delete", extra={"status":"ok"})
    deleted_student = await remove_student(id)
    if deleted_student:
        return ResponseModel(
            "Student with ID: {} removed".format(id), "Student deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Student with id {0} doesn't exist".format(id)
    )
