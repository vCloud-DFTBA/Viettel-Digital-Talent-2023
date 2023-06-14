from pydantic import BaseModel
from bson import ObjectId
from typing import Optional


class Student(BaseModel):
    stt: int
    name: str
    username: str
    year_of_birth: int
    gender: str
    university: str
    major: str

    class Config:
        schema_extra = {
            "example": {
                "stt": "100",
                "name": "Minh dep trai",
                "username" : "minhletrong",
                "year_of_birth": "2000",
                "gender": "male",
                "university": "ITMO",
                "major": "CS",
            }
        }


def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "stt": student["stt"],
        "name": student["name"],
        "username": student["username"],
        "year_of_birth": student["year_of_birth"],
        "gender": student["gender"],
        "university": student["university"],
        "major": student["major"],
    }


class UpdateStudent(BaseModel):
    stt: Optional[int]
    name: Optional[str]
    username: Optional[str]
    year_of_birth: Optional[int]
    gender: Optional[str]
    university: Optional[str]
    major: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "stt": "100",
                "name": "Minh dep trai",
                "username" : "minhletrong",
                "year_of_birth": "2000",
                "gender": "male",
                "university": "ITMO",
                "major": "CS",
            }
        }


def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
