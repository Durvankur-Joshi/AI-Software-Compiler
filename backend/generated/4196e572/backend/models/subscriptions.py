
from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Subscriptions(Base):

    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    plan = Column(String)
    status = Column(String)
    expires_at = Column(String)
    created_at = Column(String)
