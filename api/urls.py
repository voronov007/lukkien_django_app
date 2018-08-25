from django.conf.urls import url

from .views import LukkienGraphQLView

urlpatterns = [
    url(r'^$', LukkienGraphQLView, name='graphql'),
]
