from fastapi import APIRouter

router = APIRouter()

@router.get("/admin/users")
def get_admin():
    return {"message": "Generated endpoint"}

@router.put("/admin/users/{id}")
def put_admin():
    return {"message": "Generated endpoint"}

@router.delete("/admin/users/{id}")
def delete_admin():
    return {"message": "Generated endpoint"}
