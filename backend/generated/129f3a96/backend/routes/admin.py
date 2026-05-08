
from fastapi import APIRouter

router = APIRouter()


@router.get("/admin/analytics")
def get__admin_analytics():

    return {
        "message": "/admin/analytics works"
    }
