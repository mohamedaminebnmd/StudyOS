from django.utils import timezone
from . import models

def get_points(task):
    today = timezone.now().date()
    if task.status == models.Task.Status.COMPLETED and task.completed_at and task.completed_at < timezone.now().date():
        return 0
    score = 0
    if task.status == models.Task.Status.PASSED or (models.Task.Status.COMPLETED and task.completed_at and task.completed_at == timezone.now().date()):
        score += 5
    if task.goal and task.goal.priority == models.Goal.Priority.HIGH:
        score += 3
    elif task.goal and task.goal.priority == models.Goal.Priority.MEDIUM:
        score += 1
    if task.goal and task.goal.deadline:
        days_left = (task.goal.deadline - today).days
    if days_left <= 3:
        score += 10
    elif 3 < days_left <= 7:
        score += 5
    elif days_left > 7:
        score += 1
    return score

def get_today_tasks(day,tasks):
    active_tasks = [t for t in tasks if not (t.status == models.Task.Status.COMPLETED and t.completed_at and t.completed_at < timezone.now().date())]
    sorted_tasks = sorted(active_tasks, key=get_points,reverse=True)
    selected_tasks = []
    used_time = 0
    available_time = day.time_dispo 
    for task in sorted_tasks:
        if used_time + task.period <= available_time:
            selected_tasks.append(task)
            used_time += task.period
    return selected_tasks