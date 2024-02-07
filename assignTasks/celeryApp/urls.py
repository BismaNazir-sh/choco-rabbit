from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('start-task/', views.start_task, name='start_task'),
    path('update-progress/', views.update_progress, name='update_progress'),
    path('webhook/', views.webhook, name='webhook'),
]
