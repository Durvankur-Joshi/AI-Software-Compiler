
from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Activities(Base):

    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    contact_id = Column(String)
    user_id = Column(String)
    type = Column(String)
    description = Column(String)
    timestamp = Column(String)
