from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_db
from src.reminder.service import create_reminder
from src.reminder.schemas import ReminderCreate, ReminderOut
from typing import Annotated

router = APIRouter(prefix="/reminders", tags=["Reminders"])

@router.post("/", response_model=ReminderOut)
async def create_task(
    data: Annotated[ReminderCreate, Depends()],
    db: AsyncSession = Depends(get_db)
):
    reminder = await create_reminder(
        db, 
        data.text, 
        data.run_at, 
        data.periodic, 
        data.days_of_week, 
        data.time_of_day
    )
    return reminder 
