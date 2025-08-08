from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from record.models import Customer


@login_required
@require_http_methods(["GET"])
def index_customer_view(request):
    customers = Customer.objects.all().order_by("name")
    paginator = Paginator(customers, 10)  # Show 10 customers per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "record/customer/index.html",
        {
            "page_obj": page_obj,
        },
    )


@login_required
def detail_customer_view(request, pk):
    return HttpResponse(f"Details of customer {pk}")


@login_required
def create_customer_view(request):
    return HttpResponse("Create a new customer")


@login_required
def update_customer_view(request, pk):
    return HttpResponse(f"Update customer {pk}")


@login_required
def delete_customer_view(request, pk):
    return HttpResponse(f"Delete customer {pk}")


@require_http_methods(["GET"])
def search_customer_view(request):
    query = request.GET.get("q", "")
    customers = Customer.objects.filter(name__icontains=query).order_by("name")
    paginator = Paginator(customers, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "record/customer/search.html",
        {
            "page_obj": page_obj,
            "search_query": query,
        },
    )


"__all__" == [
    "index_customer_view",
    "detail_customer_view",
    "create_customer_view",
    "update_customer_view",
    "delete_customer_view",
    "search_customer_view",
]
