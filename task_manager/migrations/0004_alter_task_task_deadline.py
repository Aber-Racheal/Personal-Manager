# Generated by Django 5.1.5 on 2025-02-10 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0003_remove_task_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
