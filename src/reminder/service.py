from src.reminder.tasks import print_reminder
from src.reminder.models import Reminder 
from sqlalchemy.ext.asyncio import AsyncSession
from src.celery_app import celery
from datetime import datetime
from celery.schedules import crontab

async def create_reminder(
        db: AsyncSession,
        text: str,
        run_at: str,
        periodic=False,
        days_of_week=None,
        time_of_day=None
):
    reminder = Reminder(
        text=text,
        periodic=periodic,
        days_of_week=",".join(map(str, days_of_week)) if days_of_week else None,
        time_of_day=time_of_day.strftime("%H:%M") if time_of_day else None
    )
    db.add(reminder)
    await db.commit()
    await db.refresh(reminder)


    if periodic and days_of_week and time_of_day:
        for day in days_of_week:
            celery.add_periodic_task(
                crontab(
                    hour=time_of_day.hour,
                    minute=time_of_day.minute,
                    day_of_week=day
                ),
            print_reminder.s(text),
            name=f"reminder_{reminder.id}_{day}"
        )
    elif run_at:
        celery.send_task("print_reminder", args=[text], eta=datetime.fromisoformat(run_at))
    
    return reminder