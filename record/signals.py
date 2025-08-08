from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Service


@receiver(pre_save, sender=Service)
def set_name_lowercase(sender, instance, **kwargs):
    instance.title = instance.title.title()
