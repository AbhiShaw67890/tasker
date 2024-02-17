from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Teams, AssignedTasks

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=True, max_length=150)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

class TeamForm(forms.ModelForm):
    class Meta:
        model = Teams
        fields = ['name', 'team_leader', 'desc']


class AssignTaskForm(forms.ModelForm):
    class Meta:
        model = AssignedTasks
        fields = ['assigned_team', 'task_name', 'priority', 'description']
        widgets = {
            'assigned_team': forms.Select(attrs={'class': 'form-control'}),
            'task_name': forms.TextInput(attrs={'class': 'form-control'}),
            'priority': forms.Select(choices=AssignedTasks.PRIORITY_CHOICES, attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = AssignedTasks
        fields = ['assigned_team', 'task_name', 'priority', 'description']
