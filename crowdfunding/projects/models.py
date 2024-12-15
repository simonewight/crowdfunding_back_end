from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime

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
        
        # Convert date_end to datetime if it's just a date
        if isinstance(self.date_end, datetime):
            end_date = self.date_end
        else:
            end_date = datetime.combine(self.date_end, datetime.max.time())
            
        now = timezone.now()
        difference = end_date - now
        days_remaining = difference.days + (difference.seconds / 86400)
        return max(0, round(days_remaining))

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