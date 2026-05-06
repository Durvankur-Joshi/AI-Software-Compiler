from fastapi import APIRouter

from pydantic import BaseModel

from app.pipeline.orchestrator import (
    PipelineOrchestrator
)


router = APIRouter()

pipeline = PipelineOrchestrator()


class PromptRequest(BaseModel):

    prompt: str


@router.post("/generate")
def generate(request: PromptRequest):

    return pipeline.run(request.prompt)