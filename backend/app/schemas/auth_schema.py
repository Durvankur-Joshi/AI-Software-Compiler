from pydantic import BaseModel
from typing import List


class PermissionSchema(BaseModel):

    role: str

    allowed_routes: List[str]


class AuthSchema(BaseModel):

    roles: List[str]

    permissions: List[PermissionSchema]