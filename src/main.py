from typing import Union 
from fastapi import FastAPI
from api.events import router as eventRouter
app = FastAPI()
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