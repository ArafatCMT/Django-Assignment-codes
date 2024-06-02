from django.shortcuts import render
from task.models import TaskModel

def show_task(request):
    task = TaskModel.objects.all()
    return render(request, 'show_task.html', {'form': task})
