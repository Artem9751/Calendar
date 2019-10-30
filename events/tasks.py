from datetime import datetime, date
from .models import Event
from users.models import CustomUser
from django.core.mail import send_mail
from calendar_project import settings
from calendar_project.celery import app

from celery import shared_task

@app.task
def mail():

    all_events = Event.objects.all()
    for event in all_events:
        if event.alert_time != None:
            user = CustomUser.objects.get(username=event.author)
            '''date_of_event = datetime.strptime(str(event.date)[0:10], '%Y-%m-%d')
            time_of_event = datetime.time(datetime.strptime(event.event_time, '%H:%M:%S'))
            alert = datetime.time(datetime.strptime(event.alert_time, '%H:%M:%S'))'''
            date_and_time = datetime.combine(event.date, event.event_time)
            delta = date_and_time - datetime.now()
            alert_minutes = int(event.alert_time.hour)*60 + event.alert_time.minute
            delta_minutes = delta.seconds // 60
            print(delta_minutes, alert_minutes)
            if delta_minutes == alert_minutes:
                subject = ('you have an event through ' + event.event_time)
                message = event.body
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, ]
                send_mail(subject, message, email_from, recipient_list)
            elif delta_minutes > alert_minutes:
                print('not yet')
            else:
                print('to late')