
from fastapi import APIRouter

router = APIRouter()


@router.get("/subscriptions")
def get__subscriptions():

    return {
        "message": "/subscriptions works"
    }


@router.post("/subscriptions")
def post__subscriptions():

    return {
        "message": "/subscriptions works"
    }


@router.get("/subscriptions/{id}")
def get__subscriptions_id():

    return {
        "message": "/subscriptions/{id} works"
    }


@router.put("/subscriptions/{id}")
def put__subscriptions_id():

    return {
        "message": "/subscriptions/{id} works"
    }


@router.delete("/subscriptions/{id}")
def delete__subscriptions_id():

    return {
        "message": "/subscriptions/{id} works"
    }
