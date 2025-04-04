from fastapi import APIRouter



router = APIRouter()




@router.get("/")
def readEvents():
    return {
        "items":[1,2,3]
        
    }