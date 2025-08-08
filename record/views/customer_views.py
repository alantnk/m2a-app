from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from record.models import Customer


@login_required
def index_customers_view(request):
    customers = Customer.objects.all()
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


def detail_customers_view(request, pk):
    return HttpResponse(f"Details of customer {pk}")


def create_customers_view(request):
    return HttpResponse("Create a new customer")


def update_customers_view(request, pk):
    return HttpResponse(f"Update customer {pk}")


def delete_customers_view(request, pk):
    return HttpResponse(f"Delete customer {pk}")


"__all__" == [
    "index_customers_view",
    "detail_customers_view",
    "create_customers_view",
    "update_customers_view",
    "delete_customers_view",
]
