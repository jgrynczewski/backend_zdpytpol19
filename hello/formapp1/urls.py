from django.urls import path

from formapp1 import views

app_name = 'formapp1'

urlpatterns = [
    path('register/', views.register, name='register')
]
