# Generated by Django 5.0.6 on 2024-06-02 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_taskcategory_task_model'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='category',
            field=models.ManyToManyField(to='category.taskcategory'),
        ),
    ]
