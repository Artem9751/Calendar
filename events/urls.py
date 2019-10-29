from django.urls import path
from .views import (
    EventsUpdateView,
    EventsDeleteView,
    EventsCreateView,
    EventsListView)

urlpatterns = [
    path('<int:pk>/edit/', EventsUpdateView.as_view(), name='events_edit'),
    path('<int:pk>/delete/', EventsDeleteView.as_view(), name='events_delete'),
    path('new/', EventsCreateView.as_view(), name='events_new'),
    path('', EventsListView.as_view(), name='planners_list'),
]
