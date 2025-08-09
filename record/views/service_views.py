from django.http import HttpResponse


def index_service_view(request):
    return HttpResponse("Service index view")


def create_service_view(request):
    return HttpResponse("Create service view")


def update_service_view(request, pk):
    return HttpResponse(f"Update service view for service {pk}")


def delete_service_view(request, pk):
    return HttpResponse(f"Delete service view for service {pk}")


def search_service_view(request):
    return HttpResponse("Search service view")
