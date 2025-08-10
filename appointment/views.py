from django.shortcuts import render
from django.http import HttpResponse
from .models import Schedule
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from .forms import ScheduleForm


def index(request):
    return HttpResponse("This is the appointment index page.")


def create(request):
    return HttpResponse("This is the appointment create page.")


def update(request, pk):
    return HttpResponse(
        f"This is the appointment update page for appointment {pk}."
    )  # noqa: E501


def detail(request, pk):
    return HttpResponse(
        f"This is the appointment detail page for appointment {pk}."
    )  # noqa: E501
