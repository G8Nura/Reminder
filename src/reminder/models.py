from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime 
from src.database import Base


class Reminder(Base):
    __tablename__ = "reminders"

    id = Column(Integer, primary_key = True, index = True)
    text = Column(String, nullable=False)
    run_at = Column(DateTime, nullable=True)
    periodic = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    