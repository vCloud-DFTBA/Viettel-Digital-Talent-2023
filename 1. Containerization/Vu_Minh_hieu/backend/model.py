from pydantic import BaseModel
from bson import ObjectId


class Student(BaseModel):
    stt: int
    name: str
    year_of_birth: int
    gender: str
    university: str
    major: str
