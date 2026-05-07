
from fastapi import FastAPI

from routes import analytics
from routes import contacts
from routes import admin
from routes import auth
from routes import subscriptions

app = FastAPI()

app.include_router(analytics.router)
app.include_router(contacts.router)
app.include_router(admin.router)
app.include_router(auth.router)
app.include_router(subscriptions.router)


@app.get("/")
def root():

    return {
        "message": "AI Generated Backend Running"
    }
