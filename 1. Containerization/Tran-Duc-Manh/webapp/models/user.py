from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from fastapi import Form
from dataclasses import dataclass
from enum import Enum


class ProgramType(str, Enum):
    cloud='Cloud'
    ds='Data science and AI'
    cyber = 'Cyber security'
    web = 'Web Development'
    iot = 'IoT & 5G'

class SexType(str, Enum):
    male='Nam'
    female='Nữ'
    other='Khác'
    
class UserInfoResponse(BaseModel):
    name: str
    program: str
    title: str 
    university: str 
    year: int
    sex: str
    avatar: str


class AllUserInfoResponse(BaseModel):
    users: List[UserInfoResponse]


@dataclass
class UserInfoInput:
    name: str  = Form(...)
    program: ProgramType = Form(...)
    title: str = Form(...)
    university: str = Form(...)
    year: int = Form(...)
    sex: SexType = Form(...)
