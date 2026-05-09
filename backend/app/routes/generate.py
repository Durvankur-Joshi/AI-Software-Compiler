from fastapi import APIRouter

from pydantic import BaseModel

from app.pipeline.orchestrator import (
    PipelineOrchestrator
)
from fastapi import HTTPException


router = APIRouter()

pipeline = PipelineOrchestrator()


class PromptRequest(BaseModel):

    prompt: str


@router.post("/generate")
def generate(request: PromptRequest):

    try:

        return pipeline.run(request.prompt)

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )