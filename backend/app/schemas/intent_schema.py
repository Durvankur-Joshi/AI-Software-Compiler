from pydantic import BaseModel
from typing import List


class IntentSchema(BaseModel):

    app_name: str
    app_type: str

    features: List[str]

    user_roles: List[str]