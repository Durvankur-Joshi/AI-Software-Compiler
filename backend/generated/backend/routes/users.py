
from fastapi import APIRouter

router = APIRouter()


@router.get("/users")
def get__users():

    return {
        "message": "/users works"
    }


@router.get("/users/{user_id}")
def get__users_user_id():

    return {
        "message": "/users/{user_id} works"
    }
