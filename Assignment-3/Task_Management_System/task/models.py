from django.db import models
from category.models import TaskCategory
# Create your models here.
class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=30)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateField()

    category = models.ManyToManyField(TaskCategory)

    def __str__(self):
        return self.taskTitle
