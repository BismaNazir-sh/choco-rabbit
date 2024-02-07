from celery import shared_task
import time

@shared_task
def long_running_task(task_id):
    total_steps = 100
    for i in range(total_steps):
        time.sleep(0.1)  # Simulating some work
        progress = (i + 1) / total_steps * 100
    return 'Task Completed!'
