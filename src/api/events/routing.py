from fastapi import APIRouter,Depends,HTTPException,Query
from .schemas import (EventUpdateSchema,EventBucketSchemas)
from .models import EventModel,get_utc_now,EventCreateSchema
from typing import List
import os
from sqlmodel import Session,select
from api.db.session import get_session
router = APIRouter()
from timescaledb.hyperfunctions import time_bucket
from sqlalchemy import func,case
from datetime import datetime,timedelta,timezone
DEFAULT_LOOKUP_PAGES = [
        "/", "/about", "/pricing", "/contact", 
        "/blog", "/products", "/login", "/signup",
        "/dashboard", "/settings"
    ]

# Get data here
# List View
# GET /api/events/
@router.get("/", response_model=List[EventBucketSchemas])
def read_events(
        duration: str = Query(default="1 day"),
        pages: List = Query(default=None),
        session: Session = Depends(get_session)
    ):
    # a bunch of items in a table
    os_case = case(
        (EventModel.user_agent.ilike('%windows%'), 'Windows'),
        (EventModel.user_agent.ilike('%macintosh%'), 'MacOS'),
        (EventModel.user_agent.ilike('%iphone%'), 'iOS'),
        (EventModel.user_agent.ilike('%android%'), 'Android'),
        (EventModel.user_agent.ilike('%linux%'), 'Linux'),
        else_='Other'
    ).label('operating_system')

    bucket = time_bucket(duration, EventModel.time)
    lookup_pages = pages if isinstance(pages, list) and len(pages) > 0 else DEFAULT_LOOKUP_PAGES
    query = (
        select(
            bucket.label('bucket'),
            os_case,
            EventModel.page.label('page'),
            func.avg(EventModel.duration).label("avg_duration"),
            func.count().label('count')
        )
        .where(
            EventModel.page.in_(lookup_pages)
        )
        .group_by(
            bucket,
            os_case,
            EventModel.page,
        )
        .order_by(
            bucket,
            os_case,
            EventModel.page,
        )
    )
    raw_results = session.exec(query).fetchall()
    formatted_results = []
    for result in raw_results:
        # Create a dictionary with the correct field names
        item = EventBucketSchemas(
            bucket=result[0],  # datetime
            operating_system=result[1],  # OS
            page=result[2],  # page 
            avg_duration=result[3],  # avg_duration
            count=result[4]  # count
        )
        formatted_results.append(item)
    
    return formatted_results


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
    obj.updated_at=get_utc_now()
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj