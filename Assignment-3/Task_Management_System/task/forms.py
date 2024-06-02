from django import forms
from task.models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'

        labels = {
            'taskTitle' : 'Task Title',
            'taskDescription': 'Task Description',
            'is_completed' : 'Is_Completed',
            'task_assign_date': 'Task Assign Date'
        }

        widgets = {
            'task_assign_date': forms.DateInput(attrs={'type': 'date'}),
            'taskTitle' : forms.TextInput()
        }