from fastapi import FastAPI
from src.reminder.routers import router as reminder_router

app = FastAPI(title="Reminder App")
app.include_router(reminder_router)
