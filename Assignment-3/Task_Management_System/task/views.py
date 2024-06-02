from django.shortcuts import render, redirect
from task.forms import TaskForm
from task.models import TaskModel
# Create your views here.
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            # print(form.cleaned_data)
            return redirect ('add_task')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def delete_task(request, id):
    TaskModel.objects.get(pk = id).delete()
    return redirect('show_task')


def edit_task(request, id):
    task = TaskModel.objects.get(pk = id)
    edit_task = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_task')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': edit_task})