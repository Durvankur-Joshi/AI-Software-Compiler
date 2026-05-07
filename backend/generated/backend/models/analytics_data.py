
from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Analytics_data(Base):

    __tablename__ = "analytics_data"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String)
    metric_name = Column(String)
    metric_value = Column(String)
    user_id = Column(String)
