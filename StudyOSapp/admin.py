from django.contrib import admin
from . import models

@admin.register(models.Goal)
class AdminGoal(admin.ModelAdmin):
    fields = ['title','deadline','priority']
    list_display = ['id','title','deadline','date_created','priority']
    search_fields = ['title']
    list_filter = ['date_created','priority']
    ordering = ['-deadline', 'priority']

@admin.register(models.Task)
class AdminTask(admin.ModelAdmin):
    list_display = ['id','name', 'period','date_created','status', 'completed_at', 'goal']
    search_fields = ['name']
    ordering = ['period']
    list_filter = ['date_created', 'status']

@admin.register(models.Day)
class AdminDay(admin.ModelAdmin):
    list_display = ['day','time_dispo']
    list_filter = ['day']

