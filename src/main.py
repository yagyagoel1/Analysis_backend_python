from typing import Union 
from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def read_root():
    return {
        "Hello":"World"
    }


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
