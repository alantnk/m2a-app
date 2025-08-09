from django import forms
from .models import Customer, Service, Professional


class CustomerForm(forms.Form):
    name = forms.CharField(
        label="Nome",
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Nome do Cliente"}),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"placeholder": "Email do Cliente"}),
    )
