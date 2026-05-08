
from fastapi import FastAPI

from routes import patients
from routes import auth
from routes import doctors
from routes import appointments

app = FastAPI()

app.include_router(patients.router)
app.include_router(auth.router)
app.include_router(doctors.router)
app.include_router(appointments.router)


@app.get("/")
def root():

    return {
        "message": "AI Generated Backend Running"
    }
