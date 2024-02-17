from django.contrib.auth.models import User
from django.db import models
from datetime import date


# Create your models here.
class Teams(models.Model):
    name = models.CharField(max_length=250)
    team_leader = models.CharField(max_length=250)
    desc = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Teams"


class AssignedTasks(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('mid', 'Mid'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]

    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks')
    assigned_team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='tasks')
    task_name = models.CharField(max_length=255)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='low')
    description = models.TextField()
    assignedDate = models.DateField(default=date.today)

    def __str__(self):
        return self.task_name
    class Meta:
        verbose_name_plural = "Assigned Tasks"


