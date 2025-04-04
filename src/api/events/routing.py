from fastapi import APIRouter
from .schemas import EventSchemas
from .schemas import EventListSchemas

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
def create_event(data:dict ={})-> EventSchemas:
    print(data)
    return {"id":data.get("id")}
  
@router.put("/{event_id}")
def update_event(event_id:int,payload:dict={})-> EventSchemas:
    print(payload,"payload")
    print(event_id)
    return {"id":event_id}