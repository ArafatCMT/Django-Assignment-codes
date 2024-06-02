from django.urls import path
from task.views import add_task, delete_task, edit_task
urlpatterns = [
    path('add/', add_task, name = 'add_task'),
    path('delete_task/<int:id>', delete_task, name = 'delete_task'),
    path('edit_task/<int:id>', edit_task, name = 'edit_task'),
]