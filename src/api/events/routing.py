from fastapi import APIRouter,Depends,HTTPException
from .schemas import (EventSchemas,EventListSchemas,EventCreateSchema,EventUpdateSchema)
from .models import EventModel
import os 
from sqlmodel import Session,select
from api.db.session import get_session

router = APIRouter()
from api.db.config import DATABASE_URL



@router.get("/",response_model=EventListSchemas)
def readEvents(session:Session= Depends(get_session)):
    query = select(EventModel).order_by(EventModel.id.desc()).limit(10)
    results = session.exec(query).all()
    return {
        "results":results,
        "count":len(results)
    }

@router.get("/{event_id}",response_model=EventModel)
def get_event(event_id:int,session:Session=Depends(get_session)) :
    query = select(EventModel).where(EventModel.id == event_id)
    result  =  session.exec(query).first()
    if result ==None:
        raise HTTPException(status_code=404,detail="event not found")
    return result


@router.post("/")
def create_event(data: EventCreateSchema,session:Session = Depends(get_session))-> EventModel:
    print(data)
    print(data.page)
    print(data.model_dump())
    payload = data.model_dump()
    obj  = EventModel.model_validate(payload)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj 
  
@router.put("/{event_id}")
def update_event(event_id:int,payload:EventUpdateSchema,session:Session=Depends(get_session))-> EventModel:
    query = select(EventModel).where(EventModel.id == event_id)
    obj  =  session.exec(query).first()
    if obj ==None:
        raise HTTPException(status_code=404,detail="event not found")
    data =payload.model_dump()
    for k,v in data.items():
        setattr(obj,k,v)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj