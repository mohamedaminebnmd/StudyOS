from django.db import models

class Goal(models.Model):
    title = models.CharField()
    deadline = models.DateField()
    class Priority(models.TextChoices):
        HIGH = 'High'
        MEDIUM = 'Medium'
        LOW = 'Low'
    priority = models.CharField(choices=Priority)
    date_created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title

class Task(models.Model):
    name = models.CharField()
    period = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    class Status(models.TextChoices):
        NEW = 'New'
        PASSED = 'Passed'
        COMPLETED = 'Completed'
    status = models.CharField(choices=Status, default=Status.NEW)
    completed_at = models.DateField(null=True,blank=True)
    def __str__(self):
        return self.name

class Day(models.Model):
    day = models.DateField(unique=True, auto_now=True) 
    time_dispo = models.IntegerField()
    is_sorted = models.BooleanField(default=False)

