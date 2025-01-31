from django.contrib.auth.models import User
from django.db import models

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title

