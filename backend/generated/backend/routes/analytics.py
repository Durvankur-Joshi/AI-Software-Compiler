
from fastapi import APIRouter

router = APIRouter()


@router.get("/analytics")
def get__analytics():

    return {
        "message": "/analytics works"
    }
