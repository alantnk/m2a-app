from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Schedule
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from .forms import ScheduleForm, FilterForm
from django.db.models import Q


def index(request):
    schedules = Schedule.objects.all().order_by("-date_time")
    filter_form = FilterForm(request.GET or None)

    if filter_form.is_valid():
        status = filter_form.cleaned_data.get("status")
        start_date = filter_form.cleaned_data.get("start_date")
        end_date = filter_form.cleaned_data.get("end_date")
        filter_conditions = (Q(date_time__range=(start_date, end_date))) & (
            Q(status=status) if status != "all" else Q()
        )
        schedules = schedules.filter(filter_conditions)

    paginator = Paginator(schedules, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "filter_form": filter_form,
        "start_date": filter_form.data.get("start_date"),
        "end_date": filter_form.data.get("end_date"),
        "status": filter_form.data.get("status"),
    }
    return render(request, "appointment/index.html", context)


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
