from django.shortcuts import render
from django.http import JsonResponse
import requests

def index(request):
    return render(request, 'index.html')

def start_task(request):
    return JsonResponse({'status': 'Task execution started'}, status=200)

def update_progress(request):
    progress = 50
    return JsonResponse({'progress': progress})
