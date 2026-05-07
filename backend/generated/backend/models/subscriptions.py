
from pydantic import BaseModel


class SubscriptionsModel(BaseModel):

    contact_id: str
    plan_type: str
    start_date: str
    end_date: str
    status: str
