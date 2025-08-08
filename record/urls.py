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
        "customers/<int:pk>/",
        views.detail_customer_view,
        name="detail_customer",
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

urlpatterns = customer_urls
