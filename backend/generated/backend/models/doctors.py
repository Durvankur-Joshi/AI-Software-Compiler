
from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Doctors(Base):

    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    specialization = Column(String)
    contact_number = Column(String)
    email = Column(String)
