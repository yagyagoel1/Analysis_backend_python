from pydantic import BaseModel
from typing import List,Optional
from datetime import datetime 
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





class EventBucketSchemas(BaseModel):
    bucket: datetime
    page: str
    ua: Optional[str] = ""
    operating_system: Optional[str] = ""
    avg_duration: Optional[float] = 0.0
    count: int
