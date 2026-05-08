
from fastapi import APIRouter

router = APIRouter()


@router.get("/doctors")
def get__doctors():

    return {
        "message": "/doctors works"
    }


@router.post("/doctors")
def post__doctors():

    return {
        "message": "/doctors works"
    }


@router.get("/doctors/{id}")
def get__doctors_id():

    return {
        "message": "/doctors/{id} works"
    }


@router.put("/doctors/{id}")
def put__doctors_id():

    return {
        "message": "/doctors/{id} works"
    }


@router.delete("/doctors/{id}")
def delete__doctors_id():

    return {
        "message": "/doctors/{id} works"
    }
