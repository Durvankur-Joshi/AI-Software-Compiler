
from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Projects(Base):

    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    team_id = Column(String)
    deadline = Column(String)
