from django.urls import path

from formapp4 import views

app_name = 'formapp4'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('tasks-list/', views.tasks_list, name='tasks_list'),
]