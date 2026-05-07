
from fastapi import APIRouter

router = APIRouter()


@router.post("/projects")
def post__projects():

    return {
        "message": "/projects works"
    }


@router.get("/projects")
def get__projects():

    return {
        "message": "/projects works"
    }


@router.get("/projects/{project_id}")
def get__projects_project_id():

    return {
        "message": "/projects/{project_id} works"
    }


@router.put("/projects/{project_id}")
def put__projects_project_id():

    return {
        "message": "/projects/{project_id} works"
    }


@router.delete("/projects/{project_id}")
def delete__projects_project_id():

    return {
        "message": "/projects/{project_id} works"
    }
