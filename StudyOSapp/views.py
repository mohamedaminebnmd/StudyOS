from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from . import models, form
from . import logic
import datetime
def home(request):
    today = timezone.now().date()
    models.Task.objects.filter(date_created__lt = today,status = models.Task.Status.NEW).update(status = models.Task.Status.PASSED)
    queryset_day = models.Day.objects.filter(day = today).first()
    if not queryset_day:
        return redirect('studyos:add-day')
    else:
        queryset_tasks = models.Task.objects.select_related("goal").all()
        tasks = logic.get_today_tasks(queryset_day,queryset_tasks)
        queryset_day.save()
    context = {
        'day': queryset_day,
        'tasks': tasks
    }
    return render(request, 'studyos/home.html', context)

def add_goal(request):
    if request.method == 'POST':
        goalform = form.GoalForm(request.POST)
        if goalform.is_valid():
            instant_goal = goalform.save(commit=False)
            instant_goal.save()
            return redirect ('studyos:goal-detail', pk=instant_goal.pk)
    else:
        goalform = form.GoalForm()
    context = {
        'form': goalform
    }
    return render(request,'studyos/addgoal.html',context)

def goal(request,pk):
    goal = get_object_or_404(models.Goal,pk=pk)
    tasks = []
    if isinstance(goal, models.Goal):
       tasks = models.Task.objects.filter(goal = goal)
    tasks_number = len(tasks)
    context = {
        'goal': goal,
        'tasks': tasks,
        'tasks_number': tasks_number
    }
    return render(request, 'studyos/showgoal.html', context)

def add_task(request):
    if request.method == 'POST':
        taskform = form.TaskForm(request.POST)
        if taskform.is_valid():
            instance_task = taskform.save(commit=False)
            instance_task.save()
            return redirect('studyos:goal-detail', pk=instance_task.goal.pk)
    else:
        taskform = form.TaskForm()
    context = {
        'form': taskform
    }
    return render (request, 'studyos/addtask.html', context)

def add_day(request):
    if request.method == 'POST':
        dayform = form.DayForm(request.POST)
        if dayform.is_valid():
            instance_day = dayform.save(commit=False)
            instance_day.save()
            return redirect('studyos:home-page')
    else:
        dayform = form.DayForm()
    context = {
        'form': dayform
    }
    return render(request, 'studyos/addday.html', context)

def mark_task_as_completed(request, pk):
    if request.method == 'POST':
        task = models.Task.objects.filter(pk = pk).update(status = models.Task.Status.COMPLETED, completed_at = timezone.now().date())
        return redirect ('studyos:home-page')

def all_goals(request):
    queryset_goals = models.Goal.objects.all()
    context = {
        'goals': queryset_goals
    }
    return render(request, 'studyos/allgoals.html', context)
    
def delete_goal(request, pk):
    if request.method == 'POST':
        models.Goal.objects.filter(pk = pk).delete()
        return redirect('studyos:all-goals')

def delete_task(request, pk):
    if request.method == 'POST':
        task = models.Task.objects.filter(pk = pk).select_related('goal').get()
        pk = task.goal.pk
        task.delete()
        return redirect('studyos:goal-detail', pk = pk)