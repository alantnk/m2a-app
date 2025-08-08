from django.urls import path
from . import views

app_name = "record"

customer_urls = [
    path(
        "customers/",
        views.index_customers_view,
        name="index_customer",
    ),
    path(
        "customers/<int:pk>/",
        views.detail_customers_view,
        name="detail_customer",
    ),
    path(
        "customers/new/",
        views.create_customers_view,
        name="create_customer",
    ),
    path(
        "customers/<int:pk>/edit/",
        views.update_customers_view,
        name="update_customer",
    ),
    path(
        "customers/<int:pk>/delete/",
        views.delete_customers_view,
        name="delete_customer",
    ),
]

urlpatterns = customer_urls
