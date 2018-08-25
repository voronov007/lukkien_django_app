from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import CustomerForm, ShippingForm
from .models import Customer, Shipping
from .utils.forms import person_data_validation


def customer(request):
    errors = []
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            errors = person_data_validation(form.data)
            if not errors:
                customer_obj = form.save()
                response = redirect(
                    'shipping:customer_details', pk=customer_obj.pk
                )
                response["Location"] += '?new_obj=True'
                return response
    else:
        form = CustomerForm()

    data = {
        'section': {'title': "Customer Form"},
        'h1': "New customer",
        'form': form
    }
    if errors:
        data["errors"] = errors

    return render(request, 'shipping/shipping.html', data)


def customer_details(request, pk):
    new_obj = request.GET.get("new_obj")
    c = Customer.objects.filter(pk=pk).first()
    if c:
        data = {
            'section': {'title': "Customer Details"},
            'first_name': c.first_name,
            'last_name': c.last_name,
            'email': c.email
        }
        if new_obj:
            data["new_customer"] = "New customer was successfully created"

        return render(request, 'shipping/customer_details.html', data)

    return JsonResponse({"message": "Customer details not found"})


def shipping(request):
    errors = []
    if request.method == "POST":
        form = ShippingForm(request.POST)
        if form.is_valid():
            errors = person_data_validation(form.data)
            if not errors:
                shipping_obj = form.save()
                response = redirect(
                    'shipping:shipping_details', pk=shipping_obj.pk
                )
                response["Location"] += '?new_obj=True'
                return response
    else:
        form = ShippingForm()

    data = {
        'section': {'title': "Shipping Form"},
        'h1': "New shipping",
        'form': form
    }
    if errors:
        data["errors"] = errors

    return render(request, 'shipping/shipping.html', data)


def shipping_details(request, pk):
    new_obj = request.GET.get("new_obj")
    s = Shipping.objects.filter(pk=pk).first()
    if s:
        data = {
            'section': {'title': "Shipping Details"},
            'first_name': s.first_name,
            'last_name': s.last_name,
            'email': s.email,
            'city': s.city,
            'postal_code': s.postal_code,
            'street': s.street,
            'house_number': s.house_number,
        }
        if new_obj:
            data["new_shipping"] = "New shipping was successfully created"

        return render(request, 'shipping/shipping_details.html', data)

    return JsonResponse({"message": "Shipping details not found"})
