# from pydantic import BaseModel
from typing import List,Optional
from datetime import datetime,timezone
import sqlmodel
from sqlmodel import SQLModel,Field

def get_utc_now():
    return datetime.now(timezone.utc).replace(tzinfo=timezone.utc)
class EventModel(SQLModel,table=True):
    id: int = Field(default=None,primary_key=True)
    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlmodel.DateTime(timezone=True),
        nullable=False
        
    )
    updated_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlmodel.DateTime(timezone=True),
        nullable=False
        
    )
    page: Optional[str] = Field(default="")
    description: Optional[str] = Field(default="")
