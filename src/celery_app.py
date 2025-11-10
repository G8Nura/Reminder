from celery import Celery
from src.config import settings 


celery = Celery(
    "reminder", 
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)


celery.conf.timezone = "Asia/Almaty"
