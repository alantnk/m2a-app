from django.urls import path
from . import views

app_name = "system"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
]
