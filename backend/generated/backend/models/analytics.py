
from pydantic import BaseModel


class AnalyticsModel(BaseModel):

    date: str
    metric_name: str
    metric_value: str
