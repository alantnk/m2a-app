from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from record.models import Professional
from record.forms import ContactForm
from django.shortcuts import get_object_or_404
from django.contrib.messages import success, error


CREATE_SUCCESS_MESSAGE = "Profissional salvo com sucesso!"
CREATE_ERROR_MESSAGE = "Ocorreu um erro ao salvar o profissional. Por favor, verifique os dados."  # noqa: E501


@login_required
@require_GET
def index_professional_view(request):
    ordering = request.GET.get("ordering", "name")
    professional = Professional.objects.all().order_by(ordering)
    paginator = Paginator(professional, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "record/professional/index.html",
        {
            "page_obj": page_obj,
        },
    )


@login_required
def create_professional_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            Professional.objects.create(name=name, email=email)
            success(request, CREATE_SUCCESS_MESSAGE)
            return redirect(reverse("record:index_professional"))
        else:
            error(request, CREATE_ERROR_MESSAGE)
    else:
        form = ContactForm()
    return render(
        request,
        "record/professional/create.html",
        {
            "form": form,
        },
    )


@login_required
def update_professional_view(request, pk):
    professional = get_object_or_404(Professional, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            professional.name = form.cleaned_data["name"]
            professional.email = form.cleaned_data["email"]
            professional.save()
            success(request, CREATE_SUCCESS_MESSAGE)
            return redirect(reverse("record:index_professional"))
        else:
            error(
                request,
                CREATE_ERROR_MESSAGE,  # noqa: E501
            )
    else:
        form = ContactForm(
            initial={
                "name": professional.name,
                "email": professional.email,
            }
        )
    return render(
        request,
        "record/professional/update.html",
        {
            "form": form,
            "professional": professional,
        },
    )


@login_required
def delete_professional_view(request, pk):
    professional = get_object_or_404(Professional, pk=pk)
    if request.method == "POST":
        professional.delete()
        success(request, "Cliente excluído com sucesso!")
        return redirect(reverse("record:index_professional"))
    return render(
        request,
        "record/professional/delete.html",
        {
            "professional": professional,
        },
    )


@login_required
@require_GET
def search_professional_view(request):
    query = request.GET.get("q", "")
    professional = Professional.objects.filter(name__icontains=query).order_by(
        "name"
    )  # noqa: E501
    paginator = Paginator(professional, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "record/professional/search.html",
        {
            "page_obj": page_obj,
            "search_query": query,
        },
    )
