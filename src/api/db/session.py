from sqlmodel import SQLModel
import sqlmodel
from .config  import  DATABASE_URL

if DATABASE_URL =="":
    raise NotImplementedError("DATABASE_URL Needs to be set ")
engine=  sqlmodel.create_engine(DATABASE_URL)


def init_db():
    print("createing a database")
    SQLModel.metadata.create_all(engine)