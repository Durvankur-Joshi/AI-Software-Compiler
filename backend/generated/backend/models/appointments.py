
from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Appointments(Base):

    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String)
    doctor_id = Column(String)
    appointment_datetime = Column(String)
    reason = Column(String)
    status = Column(String)
