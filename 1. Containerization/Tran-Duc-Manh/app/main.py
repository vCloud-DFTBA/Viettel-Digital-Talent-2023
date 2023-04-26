from fastapi import FastAPI, Request

from api.routes.api import router as api_router
from core.events import create_start_app_handler
from core.config import API_PREFIX, DEBUG, PROJECT_NAME, VERSION
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from core.db import db_connect
import os
import logging

user_collection = db_connect['user']
BASE_URL = os.getenv("HOST_URL", 'http://localhost:8080/api/v1/media/')


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    application.include_router(api_router, prefix=API_PREFIX)
    pre_load = False
    if pre_load:
        application.add_event_handler(
            "startup", create_start_app_handler(application))
    return application


app = get_application()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
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
    except Exception as e:
        logging.error(e)
    return templates.TemplateResponse("index.html", {"request": request, "users": object_list})


@app.get("/user/{user}", response_class=HTMLResponse)
async def read_item(request: Request, user: str):
    try:
        student_object = user_collection.find_one({"name": user})
        if not student_object:
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
            return templates.TemplateResponse("index.html", {"request": request, "users": object_list})
        else:
            object_list = {
                "name": student_object.get("name"),
                "program": student_object.get("program"),
                "year": student_object.get("year"),
                "sex": student_object.get("sex"),
                "avatar": student_object.get("avatar"),
                "university": student_object.get("university"),
                "title": student_object.get("title"),
            }
            return templates.TemplateResponse("profile.html", {"request": request, "user": object_list, "base": BASE_URL})

    except Exception as e:
        logging.error(e)
    return templates.TemplateResponse("profile.html", {"request": request, "user": None})
