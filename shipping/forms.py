from django import forms

from .models import Customer, Shipping


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = (
            'first_name', 'last_name', 'phone_number', 'email', 'date_of_birth'
        )


class ShippingForm(forms.ModelForm):

    class Meta:
        model = Shipping
        fields = (
            'first_name', 'last_name', 'phone_number', 'email',
            "city", "postal_code", "street", "house_number"
        )
