from django.urls import path
from . import views

app_name = "record"

customer_urls = [
    path(
        "customers/",
        views.index_customer_view,
        name="index_customer",
    ),
    path(
        "customers/new/",
        views.create_customer_view,
        name="create_customer",
    ),
    path(
        "customers/<int:pk>/edit/",
        views.update_customer_view,
        name="update_customer",
    ),
    path(
        "customers/<int:pk>/delete/",
        views.delete_customer_view,
        name="delete_customer",
    ),
    path(
        "customers/search/",
        views.search_customer_view,
        name="search_customer",
    ),
]

professional_urls = [
    path(
        "professionals/",
        views.index_professional_view,
        name="index_professional",
    ),
    path(
        "professionals/new/",
        views.create_professional_view,
        name="create_professional",
    ),
    path(
        "professionals/<int:pk>/edit/",
        views.update_professional_view,
        name="update_professional",
    ),
    path(
        "professionals/<int:pk>/delete/",
        views.delete_professional_view,
        name="delete_professional",
    ),
    path(
        "professionals/search/",
        views.search_professional_view,
        name="search_professional",
    ),
]

urlpatterns = customer_urls + professional_urls
