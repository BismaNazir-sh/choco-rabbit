from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'^celery-progress/', include('celery_progress.urls')),
    # path('start-task/', views.start_task, name='start_task'),
    # path('update-progress/', views.update_progress, name='update_progress'),
    # path('task/', views.task, name='task'),
]
