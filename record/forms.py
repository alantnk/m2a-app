from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nome",
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Nome do Cliente"}),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"placeholder": "Email do Cliente"}),
    )


class Service(forms.Form):
    title = forms.CharField(
        label="Título",
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Nome do Serviço"}),
    )
