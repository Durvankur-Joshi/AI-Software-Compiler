
from fastapi import FastAPI

from .routes import api

app = FastAPI()

app.include_router(api.router)


@app.get("/")
def root():

    return {
        "message": "AI Generated Backend Running"
    }
