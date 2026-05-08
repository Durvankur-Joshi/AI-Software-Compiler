
from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Analytics_data(Base):

    __tablename__ = "analytics_data"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    date = Column(String)
    contacts_added = Column(Integer)
    contacts_updated = Column(Integer)
    contacts_deleted = Column(Integer)
