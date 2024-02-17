from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import TeamForm, AssignTaskForm, CustomUserCreationForm, TaskForm
from .models import AssignedTasks


# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect authenticated users
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Return an 'invalid login' error message
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  

def add_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            # Redirect to login page or home page after successful registration
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'add_user.html', {'form': form})


@login_required
def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a new URL
    else:
        form = TeamForm()
    return render(request, 'add_team.html', {'form': form})


@login_required
def assign_task(request):
    if request.method == 'POST':
        form = AssignTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.manager = request.user  # Set the manager to the current user
            task.assignedDate = date.today()  # Set the assigned date to today
            task.save()
            return redirect('home') 
    else:
        form = AssignTaskForm()  # An unbound form
    return render(request, 'assign_task.html', {'form': form})


@login_required
def home(request):
    # Filter tasks by the current logged-in user
    assigned_tasks = AssignedTasks.objects.filter(manager=request.user)
    return render(request, 'home.html', {'tasks': assigned_tasks})


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(AssignedTasks, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page or another appropriate page
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task_id': task_id})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(AssignedTasks, id=task_id, manager=request.user)  # Ensure only the manager can delete
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    else:
        return redirect('home')