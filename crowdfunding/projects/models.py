from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('Arts', 'Arts'),
        ('Music', 'Music'),
        ('Games', 'Games'),
        ('Tech', 'Tech'),
        ('Film', 'Film'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(null=True, blank=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )
    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default='Tech'
    )

    def save(self, *args, **kwargs):
        if not self.date_end:
            # Set default end date to 30 days from creation
            self.date_end = timezone.now() + timezone.timedelta(days=30)
        super().save(*args, **kwargs)

    def get_total_pledges(self):
        return sum(pledge.amount for pledge in self.project_pledges.all())

    def get_pledges_count(self):
        return self.project_pledges.count()

    def get_days_remaining(self):
        if self.date_end:
            now = timezone.now()
            time_left = self.date_end - now
            days_left = time_left.days
            return max(0, days_left)  # Don't return negative days
        return 0

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='project_pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )
    date_created = models.DateTimeField(auto_now_add=True)