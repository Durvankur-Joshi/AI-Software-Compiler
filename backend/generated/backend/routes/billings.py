
from fastapi import APIRouter

router = APIRouter()


@router.get("/billings")
def get__billings():

    return {
        "message": "/billings works"
    }


@router.post("/billings")
def post__billings():

    return {
        "message": "/billings works"
    }


@router.get("/billings/{id}")
def get__billings_id():

    return {
        "message": "/billings/{id} works"
    }


@router.put("/billings/{id}")
def put__billings_id():

    return {
        "message": "/billings/{id} works"
    }
