from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from record.models import Service
from record.forms import ServiceForm
from django.shortcuts import get_object_or_404
from django.contrib.messages import success, error
from django.http import HttpResponse


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
    return HttpResponse("Create service view")


@login_required
def update_service_view(request, pk):
    return HttpResponse(f"Update service view for service {pk}")


@login_required
def delete_service_view(request, pk):
    return HttpResponse(f"Delete service view for service {pk}")


@login_required
@require_GET
def search_service_view(request):
    return HttpResponse("Search service view")
