from fastapi import APIRouter, HTTPException, File, UploadFile, Depends
from models.user import UserInfoResponse, AllUserInfoResponse, UserInfoInput
from datetime import datetime
from core.db import db_connect
from fastapi.responses import FileResponse

import logging
import os

router = APIRouter()


MEDIA_PATH = "./media"
if not os.path.exists(MEDIA_PATH):
    os.makedirs(MEDIA_PATH)
user_collection = db_connect["user"]

@router.post(
    "/add-user",
    response_model=UserInfoResponse,
    name="user:add-user",
)

async def add_user_info(data_input: UserInfoInput = Depends()):
    if not data_input:
        raise HTTPException(
            status_code=404, detail="'data_input' argument invalid!")
    try:
        file_path = None
        student_object = user_collection.find_one({"name": data_input.name, "year": data_input.year})

        if student_object:
            logging.info("Student object exist")
        else:
            insert_result = user_collection.insert_one(
                {
                    "name": data_input.name,
                    "year": data_input.year,
                    "sex": data_input.sex,
                    "title": data_input.title,
                    "university": data_input.university
                }
            )
            student_object = user_collection.find_one(
                {"_id": insert_result.inserted_id}
            )
            logging.info("Successful insert student to DB")
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Exception: {err}")
    print(student_object)
    return UserInfoResponse(
        name=student_object.get("name"),
        year=student_object.get("year"),
        sex=student_object.get("sex"),
        university=student_object.get("university"),
        title=student_object.get("title"),
    )


@router.get(
    "/users",
    response_model=AllUserInfoResponse,
    name="user:all-users",
)
async def get_all_user():
    try:
        cursor = user_collection.find({})
        object_list = []
        for student_object in cursor:
            object_list.append(
                {
                    "name": student_object.get("name"),
                    "year": student_object.get("year"),
                    "sex": student_object.get("sex"),
                    "university": student_object.get("university"),
                    "title": student_object.get("title"),
                }
            )
        return AllUserInfoResponse(users=object_list)
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Exception: {err}")
