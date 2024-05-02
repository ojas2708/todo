from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from list.models import Task
from list.forms import *


# Create your views here.
def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {"tasks": tasks, "form": form}
    return render(request, "index.html", context)
    # return HttpResponse('this is a simple page')


def updateTask(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UpdateTaskForm(instance=task)

    context = {'form': form}
    return render(request, 'update_task.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect("/")
    context = {"item": item}
    return render(request, "delete.html", context)
