from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path('^customer/?', views.customer, name='customer')
]
