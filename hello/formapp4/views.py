from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

from formapp4.models import Task


def register(request):
    if request.method == "GET":
        return render(
            request,
            'formapp4/register.html'
        )

    elif request.method == "POST":
        task = request.POST.get('task')
        if task:
            task = Task(text=task)
            task.save()

        return redirect('formapp4:tasks_list')
        # return HttpResponseRedirect(reverse('formapp4:tasks_list'))


def tasks_list(request):
    tasks = Task.objects.all()

    return render(
        request,
        'formapp4/tasks-list.html',
        context={
            "tasks": tasks
        }
    )
