
from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Appointments(Base):

    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String)
    doctor_id = Column(String)
    appointment_time = Column(String)
    status = Column(String)
