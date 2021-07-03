from django.shortcuts import render


def register(request):
    return render(
        request,
        'formapp4/register.html'
    )


def tasks_list(request):
    return render(
        request,
        'formapp4/tasks-list.html',
        context = {
            "tasks": []
        }
    )