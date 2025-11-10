from src.celery_app import celery
import time


@celery.task
def print_reminder(text:str):
    print(f"[Напоминание] {text}")
    return True
