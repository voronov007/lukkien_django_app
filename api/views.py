from django.conf import settings
from graphene_django.views import GraphQLView

from .graphql.schema import Schema


LukkienGraphQLView = GraphQLView.as_view(
    schema=Schema, graphiql=True if settings.DEBUG else False
)
