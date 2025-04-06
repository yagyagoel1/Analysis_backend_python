from pydantic import BaseModel
from typing import List,Optional

class EventSchemas(BaseModel):
    id:int
    page: Optional[str] = ""
    description: Optional[str] = ""

class EventListSchemas(BaseModel):
    results: List[EventSchemas]

class EventCreateSchema(BaseModel):
    path: str
    page: Optional[str] = ""
    description: Optional[str] = ""

class EventUpdateSchema(BaseModel):
    description: str
