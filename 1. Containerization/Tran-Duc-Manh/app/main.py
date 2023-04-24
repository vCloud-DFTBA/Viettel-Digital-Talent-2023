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
BASE_URL  = os.getenv("HOST_URL", 'http://localhost:8080/api/v1/media/')
def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    application.include_router(api_router, prefix=API_PREFIX)
    pre_load = False
    if pre_load:
        application.add_event_handler("startup", create_start_app_handler(application))
    return application


app = get_application()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    try:
        cursor = user_collection.find({})
        object_list = []
        for document in cursor:
            object_list.append(
                {
                    "name": document.get("name"),
                    "program": document.get("program"),
                    "age": document.get("age"),
                    "hometown": document.get("hometown"),
                    "note": document.get("note"),
                    "joined_at": document.get("joined_at"),
                    "avatar": document.get("avatar"),
                    "email": document.get("email"),
                    "phone": document.get("phone"),
                    "fb": document.get("fb"),
                    "zalo": document.get("zalo"),
                    "github": document.get("github"),
                    "title": document.get("title"),
                }
            )
    except Exception as e:
        logging.error(e)
    return templates.TemplateResponse("index.html", {"request": request, "users": object_list})

@app.get("/user/{user}", response_class=HTMLResponse)
async def read_item(request: Request, user:str):
    try:
        document = user_collection.find_one({"name": user})
        if not document:
            cursor = user_collection.find({})
            object_list = []
            for document in cursor:
                object_list.append(
                    {
                        "name": document.get("name"),
                        "program": document.get("program"),
                        "age": document.get("age"),
                        "hometown": document.get("hometown"),
                        "note": document.get("note"),
                        "joined_at": document.get("joined_at"),
                        "avatar": document.get("avatar"),
                        "email": document.get("email"),
                        "phone": document.get("phone"),
                        "fb": document.get("fb"),
                        "zalo": document.get("zalo"),
                        "github": document.get("github"),
                        "title": document.get("title"),
                    }
                )
            return templates.TemplateResponse("index.html", {"request": request, "users": object_list})
        else:
            object_list = {
                    "name": document.get("name"),
                    "program": document.get("program"),
                    "age": document.get("age"),
                    "hometown": document.get("hometown"),
                    "note": document.get("note"),
                    "joined_at": document.get("joined_at"),
                    "avatar": document.get("avatar"),
                    "email": document.get("email"),
                    "phone": document.get("phone"),
                    "fb": document.get("fb"),
                    "zalo": document.get("zalo"),
                    "github": document.get("github"),
                    "title": document.get("title"),
                }
            return templates.TemplateResponse("profile.html", {"request": request, "user": object_list, "base": BASE_URL})
            
    except Exception as e:
        logging.error(e)
    return templates.TemplateResponse("profile.html", {"request": request, "user": None})