from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime, date

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_end = models.DateField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )
    category = models.CharField(max_length=100, null=True, blank=True)

    def get_days_remaining(self):
        if not self.date_end:
            return 0
        
        today = date.today()
        difference = self.date_end - today
        return max(0, difference.days)

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )
    date_created = models.DateTimeField(auto_now_add=True)