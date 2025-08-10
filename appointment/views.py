from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Schedule
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from .forms import ScheduleForm


def index(request):
    schdules = Schedule.objects.all().order_by("-date", "-time")
    paginator = Paginator(schdules, 10)  # Show 10 schedules per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "appointment/index.html", {"page_obj": page_obj})


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
