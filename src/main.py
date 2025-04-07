from typing import Union 
from fastapi import FastAPI
from contextlib  import asynccontextmanager
from api.db.session import init_db
from api.events import router as eventRouter



@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield 


app = FastAPI(lifespan=lifespan)
app.include_router(eventRouter,prefix="/api/events")
@app.get("/items/{item_id}")
def getItemUsingId(item_id):
    return {
        "item":[
            "ram","shyam"
        ],
        "love":{
            "lovable":item_id
        }
    }

@app.get("/healthz")
def Heallthz():
    return {
        "Status":"OK"
    }