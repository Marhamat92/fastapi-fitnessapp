from datetime import datetime

from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Integer, Text, String, TIMESTAMP, func, JSON, Date, DateTime
from sqlalchemy.dialects.postgresql import INET

from base_engine import Base

router = APIRouter()


class FitnessApp(BaseModel):
    member_name:str
    member_surname:str
    member_email:str
    member_city:str
    member_age:str

class mMemberTemplate(Base):
    __tablename__ = "member_details"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    member_name=Column(String)
    member_surname=Column(String)
    member_email=Column(String)
    member_city=Column(String)
    member_age=Column(String)

