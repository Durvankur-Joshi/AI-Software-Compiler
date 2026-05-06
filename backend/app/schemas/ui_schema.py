from pydantic import BaseModel
from typing import List


class ComponentSchema(BaseModel):

    type: str

    props: dict


class PageSchema(BaseModel):

    name: str

    components: List[ComponentSchema]


class UISchema(BaseModel):

    pages: List[PageSchema]