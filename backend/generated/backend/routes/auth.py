from fastapi import APIRouter

router = APIRouter()

@router.post("/auth/register")
def post_auth():
    return {"message": "Generated endpoint"}

@router.post("/auth/login")
def post_auth():
    return {"message": "Generated endpoint"}
