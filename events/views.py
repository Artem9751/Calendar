from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Event

#from .tasks import mail


class EventsListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'events_list.html'
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        all_events = Event.objects.filter(author=request.user)
        set_of_dates = set()
        for event in all_events:
            set_of_dates.add(event.date)
            #if event.alert_time != None:
             #   print(mail.delay(event.event_time))
        return render(request, self.template_name, {'dates': set_of_dates, 'events': all_events})


class EventsUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ('body', 'date', 'event_time', 'alert_time')
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
    fields = ('body', 'date', 'event_time', 'alert_time')
    success_url = reverse_lazy('events_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)