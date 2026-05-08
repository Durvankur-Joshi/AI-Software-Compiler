from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()


@router.get("/download-backend")
def download_backend():

    return FileResponse(
        path="generated_backend.zip",
        filename="generated_backend.zip",
        media_type="application/zip"
    )