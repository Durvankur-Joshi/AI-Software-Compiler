
from fastapi import APIRouter

router = APIRouter()


@router.get("/patients")
def get__patients():

    return {
        "message": "/patients works"
    }


@router.post("/patients")
def post__patients():

    return {
        "message": "/patients works"
    }


@router.get("/patients/{id}")
def get__patients_id():

    return {
        "message": "/patients/{id} works"
    }


@router.put("/patients/{id}")
def put__patients_id():

    return {
        "message": "/patients/{id} works"
    }


@router.delete("/patients/{id}")
def delete__patients_id():

    return {
        "message": "/patients/{id} works"
    }
