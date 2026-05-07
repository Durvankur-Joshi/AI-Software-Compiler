
from fastapi import APIRouter

router = APIRouter()


@router.post("/teams")
def post__teams():

    return {
        "message": "/teams works"
    }


@router.get("/teams")
def get__teams():

    return {
        "message": "/teams works"
    }


@router.get("/teams/{team_id}")
def get__teams_team_id():

    return {
        "message": "/teams/{team_id} works"
    }


@router.put("/teams/{team_id}")
def put__teams_team_id():

    return {
        "message": "/teams/{team_id} works"
    }


@router.delete("/teams/{team_id}")
def delete__teams_team_id():

    return {
        "message": "/teams/{team_id} works"
    }


@router.post("/teams/{team_id}/members")
def post__teams_team_id_members():

    return {
        "message": "/teams/{team_id}/members works"
    }


@router.get("/teams/{team_id}/members")
def get__teams_team_id_members():

    return {
        "message": "/teams/{team_id}/members works"
    }
