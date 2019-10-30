from datetime import datetime, timedelta, time
from django.core.mail import send_mail
from calendar_project import settings

from celery import shared_task

@shared_task
def mail(event_date, event_time, alert_time, body, email):
    date_of_event = datetime.strptime(event_date[0:10], '%Y-%m-%d')
    time_of_event = datetime.time(datetime.strptime(event_time, '%H:%M:%S'))
    alert = datetime.time(datetime.strptime(alert_time, '%H:%M:%S'))
    date_and_time = datetime.combine(date_of_event, time_of_event)
    delta = date_and_time - datetime.now()
    alert_minutes = int(alert.hour)*60 + alert.minute
    delta_minutes = delta.seconds // 60
    print(delta_minutes, alert_minutes)
    if int(delta_minutes) == int(alert_minutes):
        subject = ('you have an event through ' + event_time)
        message = body
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)
    else:
        print('not yet')