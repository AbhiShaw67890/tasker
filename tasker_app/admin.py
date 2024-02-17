from django.contrib import admin
from tasker_app.models import Teams, AssignedTasks

# Register your models here.
admin.site.register(Teams)
admin.site.register(AssignedTasks)
