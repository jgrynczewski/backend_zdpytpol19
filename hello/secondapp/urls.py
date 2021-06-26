from django.urls import path
from secondapp import views


urlpatterns = [
    path('adam/', views.adam),
    path('ewa/', views.ewa),
    path('<str:name>/', views.welcome),
    path('welcome/<str:name>', views.welcome_template),
    path('time/show/', views.time_view),
    path('time/isitnewyear/', views.new_year),
    path('time/isitnewyearupgrade/', views.new_year_upgrade),
    path('template/fruits/', views.fruits),
    path('template/passengers/', views.passengers),
]