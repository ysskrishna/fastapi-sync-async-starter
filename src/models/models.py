from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_mixin
from src.core.database import Base


@declarative_mixin
class Timestamp:
    created_at = Column(DateTime, default=func.now(), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), server_default=func.now(), onupdate=func.now(), nullable=False)


class User(Timestamp, Base):
    __tablename__ = "users"


    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
