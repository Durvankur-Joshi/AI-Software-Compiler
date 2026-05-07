
from fastapi import FastAPI

from routes import tasks
from routes import auth
from routes import projects
from routes import teams
from routes import users

app = FastAPI()

app.include_router(tasks.router)
app.include_router(auth.router)
app.include_router(projects.router)
app.include_router(teams.router)
app.include_router(users.router)


@app.get("/")
def root():

    return {
        "message": "AI Generated Backend Running"
    }
