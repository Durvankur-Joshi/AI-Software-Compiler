
from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Doctors(Base):

    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    name = Column(String)
    specialty = Column(String)
    contact_number = Column(String)
    email = Column(String)
