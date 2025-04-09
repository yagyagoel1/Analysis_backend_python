# from pydantic import BaseModel
from typing import List,Optional
from datetime import datetime,timezone
import sqlmodel
from sqlmodel import SQLModel,Field
from timescaledb import TimescaleModel
from timescaledb.utils import get_utc_now

# def get_utc_now():
    # return datetime.now(timezone.utc).replace(tzinfo=timezone.utc)
    
#page visits

class EventModel(TimescaleModel,table=True):
    # id: int = Field(default=None,primary_key=True)
    # created_at: datetime = Field(
    #     default_factory=get_utc_now,
    #     sa_type=sqlmodel.DateTime(timezone=True),
    #     nullable=False
        
    # )
    # updated_at: datetime = Field(
    #     default_factory=get_utc_now,
    #     sa_type=sqlmodel.DateTime(timezone=True),
    #     nullable=False
        
    # )
    __chunk_time_interval__="INTERVAL 1 day"
    __drop_after__="INTERVAL 3 months"
    page: str = Field(index=True) # /about, /contact, # pricing
    user_agent: Optional[str] = Field(default="", index=True) # browser
    ip_address: Optional[str] = Field(default="", index=True)
    referrer: Optional[str] = Field(default="", index=True) 
    session_id: Optional[str] = Field(index=True)
    duration: Optional[int] = Field(default=0) 

class EventCreateSchema(SQLModel):
    page: str
    user_agent: Optional[str] = Field(default="", index=True) # browser
    ip_address: Optional[str] = Field(default="", index=True)
    referrer: Optional[str] = Field(default="", index=True) 
    session_id: Optional[str] = Field(index=True)
    duration: Optional[int] = Field(default=0) 