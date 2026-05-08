from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.runtime.project_exporter import ProjectExporter

router = APIRouter()

exporter = ProjectExporter()


@router.get("/download/{project_id}")
def download_backend(project_id: str):

    zip_path = exporter.export_backend(
        project_id
    )

    return FileResponse(
        path=zip_path,
        media_type="application/zip",
        filename=f"{project_id}.zip"
    )