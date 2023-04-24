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

class UserInfoResponse(BaseModel):
    name: str
    program: str
    title: str 
    email: str 
    phone: str 
    age: int 
    hometown: str 
    note: str 
    fb: str 
    github: str 
    zalo: str 
    avatar: Optional[str] 
    joined_at: Optional[datetime] 


class AllUserInfoResponse(BaseModel):
    users: List[UserInfoResponse]


@dataclass
class UserInfoInput:
    name: str  = Form(...)
    program: ProgramType = Form(...)
    title: str = Form(...)
    email: str = Form(...)
    phone: str = Form(...)
    age: int = Form(...)
    hometown: str = Form(...)
    note: str = Form(...)
    fb: str = Form(...)
    github: str  = Form(...)
    zalo: str  = Form(...)
    
