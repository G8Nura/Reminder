from pydantic import BaseModel 
from datetime import datetime, time
from typing import Optional 


class ReminderCreate(BaseModel):
    text: str
    run_at: Optional[str] = None
    periodic: bool = False
    days_of_week: Optional[list[int]] = None
    time_of_day: Optional[time] = None


class ReminderOut(ReminderCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
        