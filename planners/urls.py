from django.urls import path
from .views import (
    PlannersListView,
    PlannersUpdateView,
    PlannersDeleteView,
    EventsUpdateView,
    EventsDeleteView,
    PlannerCreateView,
    EventsCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/', PlannersUpdateView.as_view(), name='planners_edit'),
    path('<int:pk>/delete/', PlannersDeleteView.as_view(), name='planners_delete'),
    path('new/', PlannerCreateView.as_view(), name='planners_new'),
    path('events/<int:pk>/edit/', EventsUpdateView.as_view(), name='events_edit'),
    path('events/<int:pk>/delete/', EventsDeleteView.as_view(), name='events_delete'),
    path('events/new/', EventsCreateView.as_view(), name='events_new'),
    path('', PlannersListView.as_view(), name='planners_list'),
]