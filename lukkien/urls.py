from django.contrib import admin
from django.urls import path, include, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('', include(('shipping.urls', 'shipping'), namespace='shipping')),
    re_path('^api/?$', include(('api.urls', 'api'), namespace='api'))
]
