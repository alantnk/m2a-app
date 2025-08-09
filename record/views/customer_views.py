from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from record.models import Customer
from record.forms import ContactForm
from django.shortcuts import get_object_or_404
from django.contrib.messages import success, error


CREATE_SUCCESS_MESSAGE = "Cliente salvo com sucesso!"
CREATE_ERROR_MESSAGE = (
    "Ocorreu um erro ao salvar o cliente. Por favor, verifique os dados."  # noqa: E501
)


@login_required
@require_GET
def index_customer_view(request):
    ordering = request.GET.get("ordering", "name")
    customers = Customer.objects.all().order_by(ordering)
    paginator = Paginator(customers, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "record/customer/index.html",
        {
            "page_obj": page_obj,
        },
    )


@login_required
def create_customer_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            Customer.objects.create(name=name, email=email)
            success(request, CREATE_SUCCESS_MESSAGE)
            return redirect(reverse("record:index_customer"))
        else:
            error(request, CREATE_ERROR_MESSAGE)
    else:
        form = ContactForm()
    return render(
        request,
        "record/customer/create.html",
        {
            "form": form,
        },
    )


@login_required
def update_customer_view(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            customer.name = form.cleaned_data["name"]
            customer.email = form.cleaned_data["email"]
            customer.save()
            success(request, CREATE_SUCCESS_MESSAGE)
            return redirect(reverse("record:index_customer"))
        else:
            error(
                request,
                CREATE_ERROR_MESSAGE,  # noqa: E501
            )
    else:
        form = ContactForm(
            initial={
                "name": customer.name,
                "email": customer.email,
            }
        )
    return render(
        request,
        "record/customer/update.html",
        {
            "form": form,
            "customer": customer,
        },
    )


@login_required
def delete_customer_view(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        customer.delete()
        success(request, "Cliente excluído com sucesso!")
        return redirect(reverse("record:index_customer"))
    return render(
        request,
        "record/customer/delete.html",
        {
            "customer": customer,
        },
    )


@login_required
@require_GET
def search_customer_view(request):
    query = request.GET.get("q", "")
    customers = Customer.objects.filter(name__icontains=query).order_by("name")
    paginator = Paginator(customers, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "record/customer/search.html",
        {
            "page_obj": page_obj,
            "search_query": query,
        },
    )


"__all__" == [
    "index_customer_view",
    "detail_customer_view",
    "create_customer_view",
    "update_customer_view",
    "delete_customer_view",
    "search_customer_view",
]
