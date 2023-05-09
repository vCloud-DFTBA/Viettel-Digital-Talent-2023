from fastapi import FastAPI, Request
from core.events import create_start_app_handler
from core.config import API_PREFIX, DEBUG, PROJECT_NAME, VERSION
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os
import logging
import requests

BASE_URL = os.getenv("HOST_URL", 'http://localhost:8080')


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    # application.include_router(api_router, prefix=API_PREFIX)
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
        print(f"{BASE_URL}/api/v1/users")
        object_list = requests.get(f"{BASE_URL}/api/v1/users").json()
    except Exception as e:
        logging.error(e)
    return templates.TemplateResponse("index.html", {"request": request, "users": object_list})


@app.get("/user/{user}", response_class=HTMLResponse)
async def read_item(request: Request, user: str):
    try:
        object_list = requests.get(f"{BASE_URL}/api/v1/user/{user}").json()
        return templates.TemplateResponse("profile.html", {"request": request, "user": object_list, "base": BASE_URL})
    except Exception as e:
        logging.error(e)
    return templates.TemplateResponse("profile.html", {"request": request, "user": None})
