import datetime

from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def hello(request):
    return render(
        request,
        'hello.html'
    )


def show_time(request):
    recent_time = datetime.datetime.now()
    return HttpResponse(f"{recent_time}")


def welcome(request):
    return render(
        request,
        'welcome.html'
    )