from django.urls import path
from . import views

app_name = 'studyos'

urlpatterns = [
    path('',views.home,name='home-page'),
    path('goal/add',views.add_goal, name='add-goal'),
    path('goal/<int:pk>',views.goal,name='goal-detail'),
    path('goal/tasks',views.add_task,name='add-task'),
    path('day/add',views.add_day,name='add-day'),
    path('goals/all',views.all_goals,name='all-goals'),
    path('goal/task/<int:pk>/complete',views.mark_task_as_completed,name='complete-task'),
    path('goal/<int:pk>/delete',views.delete_goal,name='delete-goal'),
    path('goal/task/<int:pk>/delete',views.delete_task,name='delete-task')
]
