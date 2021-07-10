from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods

from crudapp.models import Task


def create(request):
    if request.method == "POST":
        new_task = request.POST.get('task')
        if new_task:
            Task.objects.create(text=new_task)

        return redirect('crudapp:read')

    return render(
        request,
        'crudapp/create.html'
    )


def read(request):
    tasks = Task.objects.all()

    return render(
        request,
        'crudapp/read.html',
        context={
            'tasks': tasks
        }
    )


def update(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        modified_task = request.POST.get('task')

        task.text = modified_task
        task.save()

        return redirect('crudapp:read')

    return render(
        request,
        'crudapp/update.html',
        context={
            'task': task
        }
    )



@require_http_methods(['POST'])
def delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()

    return redirect('crudapp:read')