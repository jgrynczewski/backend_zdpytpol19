from django.urls import path

from classapp import views

app_name = 'classapp'

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('hello2/', views.HelloView.as_view(), name='hello2'),
    path('person/<int:id>/', views.person_detail, name='person_detail'),
    path('person2/<int:id>/', views.PersonView.as_view(), name='person_detail2'),
    path('person3/<int:pk>/', views.PersonDetailView.as_view(), name='person_detail3'),
    path('create-person/', views.create_person, name='create_person'),
    path('create-person2/', views.PersonCreateView.as_view(), name='create_person2'),
    path('create-person3/', views.PersonCreateView3.as_view(), name='create_person3'),
]