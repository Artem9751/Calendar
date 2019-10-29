from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from .models import Event


class EventsListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'events_list.html'
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        all_events = Event.objects.all()
        set_of_dates = set()
        for event in all_events:
            set_of_dates.add(event.date)
        return render(request, self.template_name, {'dates': set_of_dates, 'events': all_events})


class EventsUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ('event_body', 'event_time', 'event_alert_time', 'event_planner',)
    template_name = 'events_edit.html'
    success_url = reverse_lazy('events_list')
    login_url = 'login'


class EventsDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = 'events_delete.html'
    success_url = reverse_lazy('events_list')
    login_url = 'login'


class EventsCreateView(LoginRequiredMixin, CreateView):
    model = Event
    template_name = 'events_new.html'
    fields = ('event_body', 'event_time', 'event_alert_time')
    success_url = reverse_lazy('events_list')
    login_url = 'login'