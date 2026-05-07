
from fastapi import APIRouter

router = APIRouter()


@router.post("/medical-records")
def post__medical-records():

    return {
        "message": "/medical-records works"
    }


@router.get("/medical-records")
def get__medical-records():

    return {
        "message": "/medical-records works"
    }


@router.get("/medical-records/{id}")
def get__medical-records_id():

    return {
        "message": "/medical-records/{id} works"
    }


@router.put("/medical-records/{id}")
def put__medical-records_id():

    return {
        "message": "/medical-records/{id} works"
    }


@router.delete("/medical-records/{id}")
def delete__medical-records_id():

    return {
        "message": "/medical-records/{id} works"
    }
