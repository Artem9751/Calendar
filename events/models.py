from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Event(models.Model):
    date = models.DateField()
    body = models.TextField()
    event_time = models.TimeField()
    alert_time = models.TimeField(null=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    #def alert(self):
        #return self.alert_time <= (self.event_time

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('events_detail', args=[str(self.id)])
