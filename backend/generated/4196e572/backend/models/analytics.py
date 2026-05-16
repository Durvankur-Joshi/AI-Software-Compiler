
from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Analytics(Base):

    __tablename__ = "analytics"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    metrics = Column(String)
    date_range = Column(String)
    created_at = Column(String)
