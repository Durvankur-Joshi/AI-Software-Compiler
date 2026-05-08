
from fastapi import APIRouter

router = APIRouter()


@router.get("/contacts")
def get__contacts():

    return {
        "message": "/contacts works"
    }


@router.post("/contacts")
def post__contacts():

    return {
        "message": "/contacts works"
    }


@router.get("/contacts/{id}")
def get__contacts_id():

    return {
        "message": "/contacts/{id} works"
    }


@router.put("/contacts/{id}")
def put__contacts_id():

    return {
        "message": "/contacts/{id} works"
    }


@router.delete("/contacts/{id}")
def delete__contacts_id():

    return {
        "message": "/contacts/{id} works"
    }
