
from pydantic import BaseModel


class UsersModel(BaseModel):

    username: str
    email: str
    password_hash: str
    role: str
