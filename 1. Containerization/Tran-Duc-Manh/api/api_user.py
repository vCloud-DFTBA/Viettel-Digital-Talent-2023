from fastapi import APIRouter, HTTPException, File, UploadFile, Depends
from models.user import UserInfoResponse, AllUserInfoResponse, UserInfoInput
from datetime import datetime
from core.db import db_connect
from core.config import logger
from fastapi.responses import FileResponse

import logging
import os


router = APIRouter(tags=["user"], prefix="/v1")
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
        logger.info("Fail Add user to db", extra={"service": "api", "status": "fail"})
        raise HTTPException(status_code=404, detail="'data_input' argument invalid!")
    try:
        file_path = None
        student_object = user_collection.find_one(
            {"name": data_input.name}
        )
        # if file:
        #     file_path = os.path.join(MEDIA_PATH, file.filename)
        #     with open(file_path, "wb") as f:
        #         while contents := file.file.read(1024 * 1024):
        #             f.write(contents)
        if student_object:
            logging.info("Student object exist")
        else:
            insert_result = user_collection.insert_one(
                {
                    "name": data_input.name,
                    "program": data_input.program,
                    "year": data_input.year,
                    "sex": data_input.sex,
                    "avatar": "",
                    "title": data_input.title,
                    "university": data_input.university,
                }
            )
            student_object = user_collection.find_one(
                {"_id": insert_result.inserted_id}
            )
            logger.info("Add user to db", extra={"service": "api", "status": "success"})
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Exception: {err}")
    return UserInfoResponse(
        name=student_object.get("name"),
        program=student_object.get("program"),
        year=student_object.get("year"),
        sex=student_object.get("sex"),
        avatar=student_object.get("avatar"),
        university=student_object.get("university"),
        title=student_object.get("title"),
    )


@router.get(
    "/user/{user}",
    response_model=UserInfoResponse,
    name="user:add-user",
)
async def get_user_info(user: str):
    student_object = user_collection.find_one({"name": user})
    if not student_object:
        logger.info("Fail get single user to db", extra={"service": "api", "status": "fail"})
        logging.info("Student object exist")
        return {}
    else:
        logger.info("Get user to db", extra={"service": "api", "status": "success"})
        return UserInfoResponse(
            name=student_object.get("name"),
            program=student_object.get("program"),
            year=student_object.get("year"),
            sex=student_object.get("sex"),
            avatar=student_object.get("avatar"),
            university=student_object.get("university"),
            title=student_object.get("title"),
        )


@router.post(
    "/delete-user",
    name="user:delete-user",
)
async def delete_user_info(user: str):
    student_object = user_collection.delete_one({"name": user})
    logger.info("Delete user to db", extra={"service": "api", "status": "success"})
    return {"status": True}


@router.post(
    "/update-user",
    response_model=UserInfoResponse,
    name="user:update-user",
)
async def update_user_info(data_input: UserInfoInput = Depends()):
    if not data_input:
        logger.info("Update user to db", extra={"service": "api", "status": "fail"})
        raise HTTPException(status_code=404, detail="'data_input' argument invalid!")
    try:
        file_path = None
        student_object = user_collection.find_one({"name": data_input.name})
        if not student_object:
            logging.info("Student object not exist")
        else:
            student_object = user_collection.find_one_and_update(
                {"name": data_input.name},
                {
                    "$set": {
                        "name": data_input.name,
                        "program": data_input.program,
                        "year": data_input.year,
                        "sex": data_input.sex,
                        "avatar": "",
                        "title": data_input.title,
                        "university": data_input.university,
                    }
                },
            )
            student_object = user_collection.find_one({"name": data_input.name})
            # print(insert_result)
            # student_object = user_collection.find_one(
            #     {"_id": insert_result.inserted_id}
            # )
            logger.info("Update user info", extra={"service": "api", "status": "success"})
    except Exception as err:
        logger.info("Fail update user info", extra={"service": "api", "status": "fail"})
        raise HTTPException(status_code=500, detail=f"Exception: {err}")
    return UserInfoResponse(
        name=student_object.get("name"),
        program=student_object.get("program"),
        year=student_object.get("year"),
        sex=student_object.get("sex"),
        avatar=student_object.get("avatar"),
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
                    "program": student_object.get("program"),
                    "year": student_object.get("year"),
                    "sex": student_object.get("sex"),
                    "avatar": student_object.get("avatar"),
                    "university": student_object.get("university"),
                    "title": student_object.get("title"),
                }
            )
        logger.info("Get all user info", extra={"service": "api", "status": "success"})
        return AllUserInfoResponse(users=object_list)
    except Exception as err:
        logger.info("Fail get all user info", extra={"service": "api", "status": "fail"})
        raise HTTPException(status_code=500, detail=f"Exception: {err}")


@router.get(
    "/media/{avatar}",
    responses={
        200: {
            "description": "A picture of a vector image.",
            "content": {
                "image/jpeg": {
                    "example": "No example available. Just imagine a picture of a vector image."
                }
            },
        }
    },
)
def image_endpoint(avatar: str):
    file_path = os.path.join(MEDIA_PATH, avatar)
    if os.path.exists(file_path):
        logger.info("Get query image", extra={"service": "api", "status": "success"})
        return FileResponse(file_path, media_type="image/jpeg", filename=avatar)
    logger.info("Fail get media", extra={"service": "api", "status": "fail"})
    return {"error": "File not found!"}
