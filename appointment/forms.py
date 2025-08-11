from datetime import datetime, timedelta
from django import forms
from .models import STATUS_CHOICES
from record.models import Customer, Professional, Service
from bootstrap_datepicker_plus.widgets import DatePickerInput

# from django.utils import timezone


class ScheduleForm(forms.Form):
    date_at = forms.DateField(
        widget=DatePickerInput(
            format="%d/%m/%Y",
            attrs={
                "autocomplete": "off",
                "class": "form-control",
            },
        ),
        label="Data",
        initial=datetime.now(),
    )
    time_at = forms.TimeField(
        widget=forms.TimeInput(
            format="%H:%M",
            attrs={
                "autocomplete": "off",
                "class": "form-control",
                "type": "time",
            },
        ),
        label="Hora",
        initial=datetime.now(),
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


class FilterForm(forms.Form):
    start_date = forms.DateField(
        widget=DatePickerInput(
            format="%d/%m/%Y",
            attrs={
                "autocomplete": "off",
                "class": "form-control",
            },
        ),
        label="Data Inicial",
        initial=(datetime.now() - timedelta(days=30)),
    )
    end_date = forms.DateField(
        widget=DatePickerInput(
            format="%d/%m/%Y",
            attrs={
                "autocomplete": "off",
                "class": "form-control",
            },
        ),
        label="Data Final",
        initial=(datetime.now() + timedelta(days=30)),
    )

    status = forms.ChoiceField(
        choices=[("all", "Todos")] + STATUS_CHOICES,
        label="Status",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError(
                "A data inicial não pode ser posterior à data final."
            )

        return cleaned_data
