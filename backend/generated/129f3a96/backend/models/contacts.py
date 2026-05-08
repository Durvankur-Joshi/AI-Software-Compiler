
from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Contacts(Base):

    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone = Column(String)
    company = Column(String)
    user_id = Column(String)
