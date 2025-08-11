from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Schedule
from django.urls import reverse
from .forms import ScheduleForm, FilterForm
from django.db.models import Q


def index(request):
    start_date = datetime.now() - timedelta(days=30)  # noqa: E501
    end_date = datetime.now() + timedelta(days=30)  # noqa: E501
    all_schedules = Schedule.objects.all().order_by("-date_time")
    status = "all"
    filter_form = FilterForm(request.GET or None)
    schedules = all_schedules.filter(date_time__range=(start_date, end_date))
    paginator = Paginator(schedules, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if filter_form.is_valid():
        start_date = filter_form.cleaned_data.get("start_date")
        end_date = filter_form.cleaned_data.get("end_date")
        status = filter_form.cleaned_data.get("status")

        if start_date and end_date:
            schedules = all_schedules.filter(
                date_time__range=(start_date, end_date)
            )  # noqa: E501

        if status and status != "all":
            schedules = all_schedules.filter(status=status)

        paginator = Paginator(schedules, 10)
        page_obj = paginator.get_page(page_number)

    return render(
        request,
        "appointment/index.html",
        {
            "filter_form": filter_form,
            "page_obj": page_obj,
            "status": status,
            "start_date": start_date,
            "end_date": end_date,
        },
    )


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
