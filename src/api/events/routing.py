from fastapi import APIRouter
from .schemas import (EventSchemas,EventListSchemas,EventCreateSchema,EventUpdateSchema)

router = APIRouter()




@router.get("/")
def readEvents()-> EventListSchemas:
    return {
        "results":[{"id":1},{"id":2},{"id":3}]

    }

@router.get("/{event_id}")
def get_event(event_id:int) -> EventSchemas:
    return {"id":event_id}


@router.post("/")
def create_event(data: EventCreateSchema)-> EventSchemas:
    print(data)
    print(data.page)
    print(data.model_dump())
    payload = data.model_dump()
    return {"id":1,**payload}
  
@router.put("/{event_id}")
def update_event(event_id:int,payload:EventUpdateSchema)-> EventSchemas:
    print(payload,"payload")
    print(event_id)
    print(payload.description)
    return {"id":event_id}