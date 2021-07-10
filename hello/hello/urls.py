"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('hello_app.urls')),
    path('first_app/', include('first_app.urls')),
    path('secondapp/', include('secondapp.urls')),
    path('monday/', include('monday.urls')),
    path('links/', include('links.urls')),
    path('inheritance/', include('inheritance.urls')),
    path('formapp1/', include('formapp1.urls')),
    path('formapp2/', include('formapp2.urls')),
    path('formapp3/', include('formapp3.urls')),
    path('formapp4/', include('formapp4.urls')),
    path('crudapp/', include('crudapp.urls')),
    path('form/', include('form.urls')),
]
