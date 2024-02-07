from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

def index(request):
    return render(request, 'index.html')

def start_task(request):
    webhook_url = 'http://localhost:8000/webhook/'  # Replace with your webhook URL
    response = requests.post(webhook_url)
    if response.ok:
        return JsonResponse({'status': 'Task execution started'}, status=200)
    else:
        return JsonResponse({'error': 'Error starting task execution'}, status=500)

def update_progress(request):
    progress = 50  # Example: 50% progress
    return JsonResponse({'progress': progress})

def webhook(request):
    progress = 0
    while progress < 100:
        progress += 10
        update_progress_webhook(progress)
    return JsonResponse({'message': 'Tasks assigned successfully'})

def update_progress_webhook(progress):
    webhook_url = 'http://localhost:8000/update-progress/'  # Replace with your update-progress URL
    payload = {'progress': progress}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    if not response.ok:
        print('Error updating progress via webhook:', response.text)
