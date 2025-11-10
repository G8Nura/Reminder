from pydantic import BaseModel
from datetime import datetime 
from typing import Optional 


class ReminderCreate(BaseModel):
    text: str
    run_at: Optional[datetime] = None
    periodic: bool = False


class ReminderOut(ReminderCreate):
    id: int
    created_at: datetime


    class Config:
        orm_mode = True
        