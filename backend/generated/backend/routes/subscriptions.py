
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
