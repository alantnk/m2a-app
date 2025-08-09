# from django.shortcuts import render
from django.http import HttpResponse


def index_professional_view(request):
    return HttpResponse("List of professionals")


def create_professional_view(request):
    return HttpResponse("Create a new professional")


def update_professional_view(request, pk):
    return HttpResponse(f"Update professional with ID {pk}")


def delete_professional_view(request, pk):
    return HttpResponse(f"Delete professional with ID {pk}")


def search_professional_view(request):
    return HttpResponse("Search for professionals")
