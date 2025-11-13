from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from src.database import Base


class Reminder(Base):
    __tablename__ = "reminders"

    id = Column(Integer, primary_key = True, index = True)
    text = Column(String, nullable=False)
    days_of_week = Column(String, nullable=True)
    time_of_day = Column(String, default=False)
    periodic = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    