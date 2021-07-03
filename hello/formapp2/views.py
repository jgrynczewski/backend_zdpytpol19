from django.shortcuts import render

TASKS = []


def register(request):
    return render(
        request,
        'formapp2/register.html',
    )


def tasks_list(request):
    task = request.POST.get('task')
    if task:
        TASKS.append(task)

    return render(
        request,
        'formapp2/tasks_list.html',
        context = {
            "tasks": TASKS
        }
    )
