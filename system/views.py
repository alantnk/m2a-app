from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_path = request.GET.get(
                    "next",
                    reverse("system:dashboard"),
                )
                return redirect(next_path)
    else:
        form = AuthenticationForm()

    return render(request, "system/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect(reverse("system:login"))


@login_required
def dashboard_view(request):
    return render(request, "system/dashboard.html")
