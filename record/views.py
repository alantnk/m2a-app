from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def index_customers_view(request):
    return HttpResponse("List of customers")


def detail_customers_view(request, pk):
    return HttpResponse(f"Details of customer {pk}")


def create_customers_view(request):
    return HttpResponse("Create a new customer")


def update_customers_view(request, pk):
    return HttpResponse(f"Update customer {pk}")


def delete_customers_view(request, pk):
    return HttpResponse(f"Delete customer {pk}")
