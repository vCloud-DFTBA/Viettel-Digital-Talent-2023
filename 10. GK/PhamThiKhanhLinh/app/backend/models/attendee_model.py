from pydantic import BaseModel

class Attendee(BaseModel):
    name: str
    username: str
    yearOfBirth: int
    sex: str
    university: str
    major: str