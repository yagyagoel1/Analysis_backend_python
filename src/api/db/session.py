from sqlmodel import SQLModel,Session
import sqlmodel
import timescaledb
from timescaledb.utils import get_utc_now
from .config  import  DATABASE_URL

if DATABASE_URL =="":
    raise NotImplementedError("DATABASE_URL Needs to be set ")
engine=  sqlmodel.create_engine(DATABASE_URL)


def init_db():
    print("createing a database")
    SQLModel.metadata.create_all(engine)
    print("creating timescale ")
    timescaledb.metadata.create_all(engine)
    


def get_session():
    with Session(engine) as session:
        yield session
    