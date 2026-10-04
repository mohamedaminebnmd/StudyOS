from django import forms
from . import models

class GoalForm(forms.ModelForm):
    class Meta:
        model = models.Goal
        fields = ['title','deadline','priority']
        labels = {
            'deadline': 'Deadline (yyyy-mm-dd)'
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['name', 'period', 'goal']
        labels = {
            'period': 'Required period (in min)'
        }

class DayForm(forms.ModelForm):
    class Meta:
        model = models.Day
        fields = ['time_dispo']
        labels = {
            'time_dispo': 'Available time (in min)'
        }