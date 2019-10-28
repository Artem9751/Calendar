from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Planner(models.Model):
    date = models.DateField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)

    def get_absolute_url(self):
        return reverse('planners_detail', args=[str(self.id)])


class Event(models.Model):
    event_planner = models.ForeignKey(Planner, on_delete=models.CASCADE)
    event_body = models.TextField()
    event_time = models.TimeField()
    event_alert_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.event_body

    def get_absolute_url(self):
        return reverse('planners_detail', args=[str(self.id)])