
from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Users(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password_hash = Column(String)
    role = Column(String)
