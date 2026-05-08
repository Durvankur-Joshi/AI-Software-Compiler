
from fastapi import APIRouter

router = APIRouter()


@router.get("/admin/users")
def get__admin_users():

    return {
        "message": "/admin/users works"
    }
