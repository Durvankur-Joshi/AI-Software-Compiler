
from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Billings(Base):

    __tablename__ = "billings"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String)
    appointment_id = Column(String)
    amount = Column(String)
    payment_status = Column(String)
    billing_date = Column(String)
