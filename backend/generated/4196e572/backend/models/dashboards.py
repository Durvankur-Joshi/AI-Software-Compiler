
from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Dashboards(Base):

    __tablename__ = "dashboards"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    data = Column(String)
    created_at = Column(String)
