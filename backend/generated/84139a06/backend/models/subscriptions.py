
from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Subscriptions(Base):

    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    plan_type = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    status = Column(String)
