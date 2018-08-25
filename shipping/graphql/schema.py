import graphene

from .resolvers import *
from .types import *


class ShippingQuery(graphene.ObjectType):
    customers = graphene.List(
        CustomerType, resolver=resolve_all_customers
    )
    shippings = graphene.List(
        ShippingType, resolver=resolve_all_shippings
    )
