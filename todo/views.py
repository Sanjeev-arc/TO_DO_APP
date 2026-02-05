
from django.shortcuts import render
from django.contrib.auth.decorators import login_required   
from todo.models import Task
from django.shortcuts import get_object_or_404,redirect
from django.utils import timezone
from django.contrib.auth.models import User
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Task


@login_required
def dashboard(request):
    today = timezone.now().date()

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")
        category = request.POST.get("category")

        # ✅ Only create when title exists
        if title and title.strip():
            Task.objects.create(
                user=request.user,
                title=title.strip(),
                description=description,
                due_date=due_date if due_date else None,
                category=category,
            )

        return redirect("dashboard")

    user_tasks = Task.objects.filter(user=request.user, is_deleted=False)

    context = {
        "tasks": user_tasks,
        "today_tasks": user_tasks.filter(due_date=today),
        "upcoming_tasks": user_tasks.filter(due_date__gt=today),
        "total_tasks": user_tasks.count(),
    }

    return render(request, "todo/dashboard.html", context)

def Home(request):
    return render(request, 'todo/home.html')

def aboutus(request):
    return render(request, 'todo/aboutus.html')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        task.is_deleted = True
        task.save()
        return redirect('dashboard')

    return redirect("dashboard")

def restore_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)

    if request.method == "POST":
        task.is_deleted = False
        task.save()
        return redirect("trash")
def trash(request):
    tasks = Task.objects.filter(user=request.user, is_deleted=True)
    return render(request, "todo/trash.html", {"tasks": tasks})
