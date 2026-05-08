
from fastapi import APIRouter

router = APIRouter()


@router.post("/auth/register")
def post__auth_register():

    return {
        "message": "/auth/register works"
    }


@router.post("/auth/login")
def post__auth_login():

    return {
        "message": "/auth/login works"
    }
