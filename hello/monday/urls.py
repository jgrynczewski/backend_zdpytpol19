from django.urls import path

from monday import views

urlpatterns = [
    path('isitmonday/', views.monday),
]
