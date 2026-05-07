
from fastapi import APIRouter

router = APIRouter()


@router.get("/admin/users")
def get__admin_users():

    return {
        "message": "/admin/users works"
    }


@router.put("/admin/users/{id}")
def put__admin_users_id():

    return {
        "message": "/admin/users/{id} works"
    }


@router.delete("/admin/users/{id}")
def delete__admin_users_id():

    return {
        "message": "/admin/users/{id} works"
    }
