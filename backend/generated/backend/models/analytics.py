
from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Analytics(Base):

    __tablename__ = "analytics"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String)
    metric_name = Column(String)
    metric_value = Column(String)
