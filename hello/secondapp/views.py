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


def new_year(request):
    is_new_year = "NIE"

    now = datetime.now()
    if now.day==1 and now.month==1:
        is_new_year = "TAK"

    return render(
        request,
        'secondapp/isitnewyear.html',
        context = {
            'is_new_year': is_new_year,
        }
    )


def new_year_upgrade(request):
    """Conditions"""
    is_new_year = False

    now = datetime.now()
    if now.day==1 and now.month==1:
        is_new_year = True

    return render(
        request,
        'secondapp/isitnewyearupgrade.html',
        context = {
            'is_new_year': is_new_year,
        }
    )

def fruits(request):
    """Loops"""
    fruits = ["jabłko", "banan", "mandarynka", "brzoskwinia"]

    return render(
        request,
        'secondapp/fruits.html',
        context={
            "fruits": fruits,
        }
    )


def passengers(request):
    return render(
        request,
        'secondapp/passengers.html',
        context={
            "passengers": [
                {"name": "Adam", "age": 40},
                {"name": "Ewa", "age": 10},
                {"name": "Jan", "age": 30}
            ]
        }
    )