from pydantic import BaseModel
from typing import List


class EndpointSchema(BaseModel):

    path: str
    method: str

    request_fields: List[str]

    response_fields: List[str]


class APISchema(BaseModel):

    endpoints: List[EndpointSchema]