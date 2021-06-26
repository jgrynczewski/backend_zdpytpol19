from datetime import datetime

from markupsafe import escape

from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def adam(request):
    return render(
        request,
        'secondapp/adam.html'
    )


def ewa(request):
    return render(
        request,
        'secondapp/ewa.html'
    )


def welcome(request, name):
    name = escape(name)
    return HttpResponse(f"Witaj, {name}!")


def welcome_template(request, name):
    return render(
        request,
        'secondapp/welcome.html',
        context = {
            "name": name,
        }
    )


def time_view(request):
    t = datetime.now()

    return render(
        request,
        'secondapp/time.html',
        context={
            "time": t
        }
    )