# from pydantic import BaseModel
from typing import List,Optional
from sqlmodel import SQLModel,Field


class EventModel(SQLModel,table=True):
    id: int = Field(default=None,primary_key=True)
    page: Optional[str] = Field(default="")
    description: Optional[str] = Field(default="")
