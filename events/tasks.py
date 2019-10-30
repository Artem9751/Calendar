from .models import Event

from celery import shared_task

@shared_task
def mail(event_time):
    messege = ('you have an event through' + event_time)
    '''message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['brilon@tut.by', ]'''
    return messege