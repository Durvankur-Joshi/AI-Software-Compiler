
from fastapi import FastAPI

from routes import contacts
from routes import subscriptions
from routes import dashboard
from routes import analytics
from routes import admin
from routes import auth

app = FastAPI()

app.include_router(contacts.router)
app.include_router(subscriptions.router)
app.include_router(dashboard.router)
app.include_router(analytics.router)
app.include_router(admin.router)
app.include_router(auth.router)


@app.get("/")
def root():

    return {
        "message": "AI Generated Backend Running"
    }
