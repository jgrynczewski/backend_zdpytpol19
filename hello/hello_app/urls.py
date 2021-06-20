from django.urls import path

from hello_app import views


urlpatterns = [
    path('hello', views.hello),
    path('time', views.show_time),
    path('welcome', views.welcome),
]