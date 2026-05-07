
from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Team_memberships(Base):

    __tablename__ = "team_memberships"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    team_id = Column(String)
