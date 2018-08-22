from django.contrib import admin
from .models import Customer, Shipping


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    pass
