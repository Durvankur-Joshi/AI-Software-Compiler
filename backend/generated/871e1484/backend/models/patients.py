
from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Patients(Base):

    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    name = Column(String)
    date_of_birth = Column(String)
    gender = Column(String)
    contact_number = Column(String)
    email = Column(String)
    address = Column(String)
