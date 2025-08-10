from django.urls import path
from . import views

app_name = "appointment"

urlpatterns = [
    path("list/", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("edit/<int:pk>/", views.update, name="update"),
    path("detail/<int:pk>/", views.detail, name="detail"),
]
