from django.shortcuts import render


def register(request):
    return render(
        request,
        'formapp3/register.html',
    )


def tasks_list(request):
    with open('tasks.txt', 'a+') as f:
        task = request.POST.get('task')
        if task:
            f.write(task+"\n")

    with open('tasks.txt', 'r') as f:
        tasks = f.readlines()

    return render(
        request,
        'formapp3/tasks_list.html',
        context = {
            "tasks": tasks
        }
    )
