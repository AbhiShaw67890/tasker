# Generated by Django 5.0.2 on 2024-02-16 19:06

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasker_app', '0002_alter_teams_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignedTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=255)),
                ('priority', models.CharField(choices=[('low', 'Low'), ('mid', 'Mid'), ('high', 'High'), ('urgent', 'Urgent')], default='low', max_length=6)),
                ('description', models.TextField()),
                ('assignedDate', models.DateField(default=datetime.date.today)),
                ('assigned_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasker_app.teams')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Assigned Tasks',
            },
        ),
    ]
