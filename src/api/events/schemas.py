from pydantic import BaseModel
from typing import List

class EventSchemas(BaseModel):
    id:int

class EventListSchemas(BaseModel):
    results: List[EventSchemas]