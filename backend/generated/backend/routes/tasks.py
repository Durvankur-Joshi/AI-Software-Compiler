
from fastapi import APIRouter

router = APIRouter()


@router.post("/tasks")
def post__tasks():

    return {
        "message": "/tasks works"
    }


@router.get("/tasks")
def get__tasks():

    return {
        "message": "/tasks works"
    }


@router.get("/tasks/{task_id}")
def get__tasks_task_id():

    return {
        "message": "/tasks/{task_id} works"
    }


@router.put("/tasks/{task_id}")
def put__tasks_task_id():

    return {
        "message": "/tasks/{task_id} works"
    }


@router.delete("/tasks/{task_id}")
def delete__tasks_task_id():

    return {
        "message": "/tasks/{task_id} works"
    }
