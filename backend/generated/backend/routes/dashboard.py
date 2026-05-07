
from fastapi import APIRouter

router = APIRouter()


@router.get("/dashboard")
def get__dashboard():

    return {
        "message": "/dashboard works"
    }
