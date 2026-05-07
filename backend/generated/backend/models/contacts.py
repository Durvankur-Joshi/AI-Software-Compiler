
from pydantic import BaseModel


class ContactsModel(BaseModel):

    first_name: str
    last_name: str
    email: str
    phone: str
    company: str
    user_id: str
