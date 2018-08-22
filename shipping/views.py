from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer
from django.http import JsonResponse


def customer(request):
    if request.method == "POST":
        return redirect('shipping:customer_details', pk=1)
    else:
        form = CustomerForm()
    return render(
        request, 'shipping/customer.html',
        {
            'section': {'title': "Customer Form"},
            'form': form
        }
    )


def customer_details(request, pk):
    c = Customer.objects.filter(pk=pk).first()
    if c:
        return render(
            request, 'shipping/customer_details.html',
            {
                'section': {'title': "Customer Form"},
                'name': c.first_name
            }
        )

    return JsonResponse({"message": "not found"})
