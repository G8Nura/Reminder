from src.celery_app import celery

@celery.task
def print_reminder(text:str):
    print(f"[Напоминание] {text}")