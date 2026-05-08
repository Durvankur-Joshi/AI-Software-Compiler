
from fastapi import APIRouter

router = APIRouter()


@router.get("/medical-records")
def get__medical-records():

    return {
        "message": "/medical-records works"
    }


@router.post("/medical-records")
def post__medical-records():

    return {
        "message": "/medical-records works"
    }


@router.get("/medical-records/{id}")
def get__medical-records_id():

    return {
        "message": "/medical-records/{id} works"
    }
