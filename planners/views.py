from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
import datetime

from .forms import PlannerCreateForm
from .models import Planner, Event


class PlannersListView(LoginRequiredMixin, ListView):
    model = Planner
    template_name = 'planners_list.html'
    login_url = 'login'

    def get(self, request):
        plans_list = Planner.objects.all()
        events_of_day = Event.objects.all()
        return render(request, self.template_name, {"plans_list": plans_list, "events_of_day": events_of_day, "username": request.user})


class PlannersUpdateView(LoginRequiredMixin, UpdateView):
    model = Planner
    fields = ('date',)
    template_name = 'planners_edit.html'
    success_url = reverse_lazy('planners_list')
    login_url = 'login'


class PlannersDeleteView(LoginRequiredMixin, DeleteView):
    model = Planner
    template_name = 'planners_delete.html'
    success_url = reverse_lazy('planners_list')
    login_url = 'login'


'''class PlannerCreateView(LoginRequiredMixin, CreateView):
    model = Planner
    template_name = 'planners_new.html'
    fields = ('date',)
    success_url = reverse_lazy('planners_list')
    login_url = 'login'

    def form_valid(self, form):
        dates = set()
        for a in self.model.objects.all():
            dates.add(a.date)
        print()
        form.instance.author = self.request.user
        return super().form_valid(form)'''


class PlannerCreateView(CreateView):
    model = Planner
    form_class = PlannerCreateForm
    template_name = 'planners_new.html'

    def post(self, request):
        newday = Planner()
        newday.date = request.POST.get("date")
        newday.author = request.user
        days = set()
        for day in Planner.objects.all():
            days.add(str(day))
        if str(newday.date) in days:
            current_day = Planner.objects.get(date = newday.date)
            error = "You already have plans for this day"
            return render(request, "error.html", {"error": error, 'current_day': current_day})
        else:
            newday.save()
            return HttpResponseRedirect('/planners/')

    def get(self, request):
        form_create = PlannerCreateForm()
        return render(request, self.template_name, {'formcreate': form_create})


class EventsUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ('event_body', 'event_time', 'event_alert_time', 'event_planner',)
    template_name = 'events_edit.html'
    success_url = reverse_lazy('planners_list')
    login_url = 'login'


class EventsDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = 'events_delete.html'
    success_url = reverse_lazy('planners_list')
    login_url = 'login'


class EventsCreateView(LoginRequiredMixin, CreateView):
    model = Event
    template_name = 'events_new.html'
    fields = ('event_body', 'event_time', 'event_alert_time', 'event_planner',)
    success_url = reverse_lazy('planners_list')
    login_url = 'login'


''' Email send
from django.core.mail import send_mail
from calendar_project import settings


 def get(self, request, *args, **kwargs):
        subject = 'Thank you for registering to our site'
        message = ' it  means a world to us '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['brilon@tut.by', ]
        send_mail(subject, message, email_from, recipient_list)
'''