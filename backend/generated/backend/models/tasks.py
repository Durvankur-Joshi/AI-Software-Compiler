
from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Tasks(Base):

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    project_id = Column(String)
    assigned_to_user_id = Column(String)
    due_date = Column(String)
    status = Column(String)
