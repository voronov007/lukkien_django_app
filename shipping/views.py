from django.shortcuts import render, redirect
from .forms import CustomerForm


def customer(request):
    if request.method == "POST":
        pass
        return redirect('customer_details', pk=1)
    else:
        form = CustomerForm()
    return render(
        request, 'shipping/customer.html',
        {
            'section': {'title': "Customer Form"},
            'form': form
        }
    )