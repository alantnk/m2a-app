from datetime import datetime, timedelta
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.messages import success, error
from .models import Schedule
from .forms import ScheduleForm, FilterForm

SAVE_SUCCESS_MESSAGE = "Agendamento salvo com sucesso."
SAVE_ERROR_MESSAGE = "Houve um erro ao criar o agendamento. Verifique o formulário e tente novamente."  # noqa: E501


@login_required
@require_GET
def index(request):
    start_date = datetime.now() - timedelta(days=30)  # noqa: E501
    end_date = datetime.now() + timedelta(days=30)  # noqa: E501
    all_schedules = Schedule.objects.all().order_by("date_time")
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
        filtered_schedules = all_schedules
        if start_date and end_date:
            filtered_schedules = filtered_schedules.filter(
                date_time__range=(start_date, end_date)
            )  # noqa: E501

        if status and status != "all":
            filtered_schedules = filtered_schedules.filter(status=status)

        paginator = Paginator(filtered_schedules, 10)
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


@login_required
def create(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            date_at = form.cleaned_data["date_at"]
            time_at = form.cleaned_data["time_at"]
            professional = form.cleaned_data["professional"]
            customer = form.cleaned_data["customer"]
            service = form.cleaned_data["service"]
            status = form.cleaned_data["status"]
            try:
                Schedule.objects.create(
                    date_time=datetime.combine(date_at, time_at),
                    professional=professional,
                    customer=customer,
                    service=service,
                    status=status,
                )
                success(request, SAVE_SUCCESS_MESSAGE)
                return redirect(reverse("appointment:index"))
            except IntegrityError:
                error(
                    request,
                    f"Existe um agendamento para {date_at} às {time_at} com o profissional {professional}.",  # noqa: E501
                )
        else:
            error(
                request,
                SAVE_ERROR_MESSAGE,
            )
    else:
        form = ScheduleForm()

    return render(request, "appointment/create.html", {"form": form})


@login_required
def update(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            date_at = form.cleaned_data["date_at"]
            time_at = form.cleaned_data["time_at"]
            professional = form.cleaned_data["professional"]
            customer = form.cleaned_data["customer"]
            service = form.cleaned_data["service"]
            status = form.cleaned_data["status"]
            try:
                schedule.date_time = datetime.combine(date_at, time_at)
                schedule.professional = professional
                schedule.customer = customer
                schedule.service = service
                schedule.status = status
                schedule.save()
                success(request, SAVE_SUCCESS_MESSAGE)
                return redirect(reverse("appointment:index"))
            except IntegrityError:
                error(
                    request,
                    f"Existe um agendamento para {date_at} às {time_at} com o profissional {professional}.",  # noqa: E501
                )

        else:
            error(request, SAVE_ERROR_MESSAGE)

    form = ScheduleForm(
        initial={
            "status": schedule.status,
            "professional": schedule.professional,
            "customer": schedule.customer,
            "service": schedule.service,
            "date_at": schedule.date_time.date(),
            "time_at": schedule.date_time.time(),
        }
    )
    return render(
        request,
        "appointment/update.html",
        {"form": form, "schedule": schedule},  # noqa: E501
    )


@login_required
def detail(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    return render(request, "appointment/detail.html", {"schedule": schedule})
