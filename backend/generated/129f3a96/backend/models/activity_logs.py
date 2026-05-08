
from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Activity_logs(Base):

    __tablename__ = "activity_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    action = Column(String)
    timestamp = Column(String)
    details = Column(String)
