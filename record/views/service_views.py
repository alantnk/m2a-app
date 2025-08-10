from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from record.models import Service
from record.forms import ServiceForm
from django.shortcuts import get_object_or_404
from django.contrib.messages import success, error

SAVE_SUCCESS_MESSAGE = "Serviço salvo com sucesso!"
SAVE_ERROR_MESSAGE = (
    "Ocorreu um erro ao salvar o serviço. Por favor, verifique os dados."  # noqa: E501
)


@login_required
@require_GET
def index_service_view(request):
    customers = Service.objects.all()
    paginator = Paginator(customers, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    print(page_obj.object_list)
    return render(
        request,
        "record/service/index.html",
        {
            "page_obj": page_obj,
        },
    )


@login_required
def create_service_view(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            try:
                Service.objects.create(title=title)
                success(request, SAVE_SUCCESS_MESSAGE)
                return redirect(reverse("record:index_service"))
            except IntegrityError:
                error(request, "Erro: Já existe um serviço com esse nome.")
        else:
            error(request, SAVE_ERROR_MESSAGE)
    else:
        form = ServiceForm()

    return render(
        request,
        "record/service/create.html",
        {
            "form": form,
        },
    )


@login_required
def update_service_view(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            service.title = title
            try:
                service.save()
                success(request, SAVE_SUCCESS_MESSAGE)
                return redirect(reverse("record:index_service"))
            except IntegrityError:
                error(request, "Erro: Já existe um serviço com esse nome.")
        else:
            error(request, SAVE_ERROR_MESSAGE)
    else:
        form = ServiceForm(initial={"title": service.title})

    return render(
        request,
        "record/service/update.html",
        {
            "form": form,
            "service": service,
        },
    )


@login_required
def delete_service_view(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == "POST":
        service.delete()
        success(request, "Serviço excluído com sucesso!")
        return redirect(reverse("record:index_service"))
    return render(
        request,
        "record/service/delete.html",
        {
            "service": service,
        },
    )


@login_required
@require_GET
def search_service_view(request):
    query = request.GET.get("q", "")
    customers = Service.objects.filter(title__icontains=query)
    paginator = Paginator(customers, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "record/service/search.html",
        {
            "page_obj": page_obj,
            "search_query": query,
        },
    )


"__all__" == [
    "index_service_view",
    "create_service_view",
    "update_service_view",
    "delete_service_view",
    "search_service_view",
]
