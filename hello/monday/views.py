from datetime import datetime

from django.shortcuts import render

# Create your views here.
def monday(request):
    is_monday = False
    now = datetime.now()

    if (now.weekday() == 0):
        is_monday = True

    return render(
        request,
        'monday/monday.html',
        context = {
            'is_monday': is_monday,
        }
    )