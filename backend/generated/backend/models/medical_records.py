
from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Medical_records(Base):

    __tablename__ = "medical_records"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String)
    doctor_id = Column(String)
    record_date = Column(String)
    diagnosis = Column(String)
    prescription = Column(String)
    notes = Column(String)
