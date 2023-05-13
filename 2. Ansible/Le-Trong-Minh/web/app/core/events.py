from typing import Callable
from fastapi import FastAPI


def preload():
    return 1

def create_start_app_handler(app: FastAPI) -> Callable:
    def start_app() -> None:
        preload()
        # continue
    return start_app
