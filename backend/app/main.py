from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.routes.generate import router

from app.routes import download


app = FastAPI(
    title="AI Compiler System"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)
app.include_router(download.router)


@app.get("/")
def home():

    return {
        "status": "running"
    }