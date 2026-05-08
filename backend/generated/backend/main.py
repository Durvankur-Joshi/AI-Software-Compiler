
from fastapi import FastAPI

from routes import appointments
from routes import doctors
from routes import auth
from routes import medical-records
from routes import billings
from routes import patients

app = FastAPI()

app.include_router(appointments.router)
app.include_router(doctors.router)
app.include_router(auth.router)
app.include_router(medical-records.router)
app.include_router(billings.router)
app.include_router(patients.router)


@app.get("/")
def root():

    return {
        "message": "AI Generated Backend Running"
    }
