from celery import shared_task
import time
from celery_progress.backend import ProgressRecorder


print("in tasks")
@shared_task(bind=True)
def long_running_task(self, sleep_time):
    print("Functon long running task")
    progress_recorder = ProgressRecorder(self)
    total_steps = 10
    for i in range(total_steps):
        time.sleep(sleep_time)  # Simulating some work
        progress_recorder.set_progress(i+1, total_steps, f'on iteration {i}')
    print("loop end in long running task")
    return 'Done!'
