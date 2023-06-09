from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from fastapi import Form
from dataclasses import dataclass
from enum import Enum

class SexType(str, Enum):
    male='Nam'
    female='Nữ'
    other='Khác'
    
class UserInfoResponse(BaseModel):
    name: str
    title: str 
    university: str 
    year: int
    sex: str
    
class AllUserInfoResponse(BaseModel):
    users: List[UserInfoResponse]


@dataclass
class UserInfoInput:
    name: str  = Form(...)
    university: str = Form(...)
    title: str = Form(...)
    year: int = Form(...)
    sex: SexType = Form(...)
    
