
from django.shortcuts import render
from django.contrib.auth.decorators import login_required   
from todo.models import Task
from django.shortcuts import get_object_or_404,redirect
from django.utils import timezone
from django.contrib.auth.models import User
# Create your views here.
@login_required
def dashboard(request): 
    today=timezone.now().date() 
    user_tasks=Task.objects.filter(user=request.user).all()
    total_tasks=user_tasks.count()
    today_tasks = user_tasks.filter(due_date=today).order_by('due_date')
    upcoming_tasks = user_tasks.filter(due_date__gt=today).order_by('due_date')
    
    
    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description','')
        due_date=request.POST.get('due_date')
        category=request.POST.get('category','General')
        Task.objects.create(user=request.user, title=title, description=description, due_date=due_date, category=category)
    tasks = Task.objects.filter(user=request.user, is_deleted=False).all()
    context = {
        'tasks': tasks,
        'today_tasks': today_tasks,
        'upcoming_tasks': upcoming_tasks,
        'total_tasks': total_tasks,
    }
    return render(request, 'todo/dashboard.html', context=context)   

def Home(request):
    return render(request, 'todo/home.html')

def aboutus(request):
    return render(request, 'todo/aboutus.html')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method=='POST':
      task.is_deleted=True
      task.save()
      return redirect('dashboard')

def restore_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)

    if request.method == "POST":
        task.is_deleted = False
        task.save()
        return redirect("trash")
def trash(request):
    tasks = Task.objects.filter(user=request.user, is_deleted=True)
    return render(request, "todo/trash.html", {"tasks": tasks})
