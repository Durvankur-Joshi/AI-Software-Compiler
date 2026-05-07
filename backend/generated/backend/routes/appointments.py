
from fastapi import APIRouter

router = APIRouter()


@router.post("/appointments")
def post__appointments():

    return {
        "message": "/appointments works"
    }


@router.get("/appointments")
def get__appointments():

    return {
        "message": "/appointments works"
    }


@router.get("/appointments/{id}")
def get__appointments_id():

    return {
        "message": "/appointments/{id} works"
    }


@router.put("/appointments/{id}")
def put__appointments_id():

    return {
        "message": "/appointments/{id} works"
    }


@router.delete("/appointments/{id}")
def delete__appointments_id():

    return {
        "message": "/appointments/{id} works"
    }
