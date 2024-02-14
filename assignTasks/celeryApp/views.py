from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from .tasks import long_running_task


def index(request):
    print("in views.index")
    result = long_running_task.delay(sleep_time=2)
    print("returned from celery fucntion")
    return render(request, 'index.html', context={'task_id': result.task_id})

# @csrf_exempt
# #@shared_task
# def start_task(request):
    # # url = 'http://127.0.0.1:8000/task/' 
    # # print("calling api in start task")
    # # response = requests.post(url)
    # # print("res", response)
    # progress = 0
    # while progress < 100:
        # progress += 10
        # url = 'http://127.0.0.1:8000/update-progress/'  
        # payload = {'progress': progress}
        # headers = {'Content-Type': 'application/json'}
        # response = requests.post(url, json=payload, headers=headers)
        # print("update response", response)
        # if not response.ok:
            # print('Error updating progress via webhook:', response.text)
    # if response.ok:       
        # return JsonResponse({'message': 'Tasks assigned successfully'})
    
    # else:
        # return JsonResponse({'error': 'Error starting task execution'}, status=500)

# @csrf_exempt
# @shared_task
# def update_progress(request):
    # # data = json.loads(request.body)
    # # print("data", data)
    # # p = data['progress']
    # # print("Progress is", p)
    # progress = 10
    # return JsonResponse({'progress': progress})

# @csrf_exempt
# @shared_task
# def task(request):
    # print("req", request)
    # if request.method == 'POST':
        # print("there")
        # progress = 0
        # while progress < 100:
            # progress += 10
            # url = 'http://127.0.0.1:8000/update-progress/'  
            # payload = {'progress': progress}
            # headers = {'Content-Type': 'application/json'}
            # response = requests.post(url, json=payload, headers=headers)
            # print("update response", response)
            # if not response.ok:
                # print('Error updating progress via webhook:', response.text)
                
        # return JsonResponse({'message': 'Tasks assigned successfully'})
    # else:
        # return JsonResponse({'error': 'Method not allowed'}, status=405)

# @csrf_exempt
# def update_progress_webhook(progress):
    # webhook_url = 'http://127.0.0.1:8000/update-progress/'  
    # payload = {'progress': progress}
    # headers = {'Content-Type': 'application/json'}
    # response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    # print("update response", response)
    # if not response.ok:
        # print('Error updating progress via webhook:', response.text)
