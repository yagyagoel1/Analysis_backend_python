from pydantic import BaseModel
from typing import List,Optional

class EventSchemas(BaseModel):
    id:int
    page: Optional[str] = ""
    description: Optional[str] = ""

class EventListSchemas(BaseModel):
    results: List[EventSchemas]
    count: int

class EventCreateSchema(BaseModel):
    page: Optional[str] = ""
    description: Optional[str] = ""

class EventUpdateSchema(BaseModel):
    description: str
