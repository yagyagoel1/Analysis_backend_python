from fastapi import APIRouter
from .schemas import (EventSchemas,EventListSchemas,EventCreateSchema,EventUpdateSchema)
from .models import EventModel
import os 

router = APIRouter()
from api.db.config import DATABASE_URL



@router.get("/")
def readEvents()-> EventListSchemas:
    print(os.environ.get("DATABASE_URL"))
    return {
        "results":[{"id":1},{"id":2},{"id":3}]

    }

@router.get("/{event_id}")
def get_event(event_id:int) -> EventModel:
    return {"id":event_id}


@router.post("/")
def create_event(data: EventCreateSchema)-> EventModel:
    print(data)
    print(data.page)
    print(data.model_dump())
    payload = data.model_dump()
    return {"id":1,**payload}
  
@router.put("/{event_id}")
def update_event(event_id:int,payload:EventUpdateSchema)-> EventModel:
    print(payload,"payload")
    print(event_id)
    print(payload.description)
    return {"id":event_id}