from django import forms
from .models import STATUS_CHOICES
from record.models import Customer, Professional, Service


class ScheduleForm(forms.Form):
    date_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        label="Data e Hora",
    )
    professional = forms.ModelChoiceField(
        queryset=Professional.objects.all(),
        label="Selecione um Profissional",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        label="Selecione um Cliente",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    service = forms.ModelChoiceField(
        queryset=Service.objects.all(),
        label="Selecione um Serviço",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        label="Status",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
