from pydantic import BaseModel
from typing import List


class EntitySchema(BaseModel):

    name: str
    fields: List[str]


class ArchitectureSchema(BaseModel):

    entities: List[EntitySchema]

    pages: List[str]

    modules: List[str]

    roles: List[str]