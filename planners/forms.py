from django import forms

from .models import Planner, Event


class PlannerCreateForm(forms.Form):
    model = Planner
    date = forms.DateField(widget=forms.DateInput)
