from typing import Union 
from fastapi import FastAPI
from contextlib  import asynccontextmanager
from api.db.session import init_db
from api.events import router as eventRouter
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield 



app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentails=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
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