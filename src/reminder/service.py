from src.reminder.tasks import print_reminder
from src.reminder.models import Reminder 
from sqlalchemy.ext.asyncio import AsyncSession


async def create_reminder(
        db: AsyncSession,
        text: str,
        run_at: None,
        periodic=False
):
    reminder = Reminder(
        text=text,
        run_at=run_at,
        periodic=periodic
    )
    db.add(reminder)
    await db.commit()
    await db.refresh(reminder)

    if run_at:
        print_reminder.apply_async((text,), eta=run_at)
    elif periodic:
        print_reminder.apply_async((text,), countdown=10)
    else:
        print_reminder.delay(text)
    
    return reminder
