from django.urls import path

from golden_thoughts import views

app_name = 'golden_thoughts'

urlpatterns = [
    path("", views.thought, name='thought'),
]