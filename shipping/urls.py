from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path('^new_customer/?$', views.customer, name='customer'),
    re_path(
        '^customer/(?P<pk>[0-9]+)/$', views.customer_details,
        name='customer_details'
    ),
]
