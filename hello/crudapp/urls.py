from django.urls import path

from crudapp import views

app_name = 'crudapp'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('read/', views.read, name='read'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]