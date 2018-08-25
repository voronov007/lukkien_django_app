import graphene

from .person import PersonType
from ...models import Shipping


class ShippingType(PersonType):
    postal_code = graphene.String()
    city = graphene.String()
    street = graphene.String()
    house_number = graphene.String()

    def resolve_postal_code(shipping: Shipping, info):
        return shipping.postal_code

    def resolve_city(shipping: Shipping, info):
        return shipping.city

    def resolve_street(shipping: Shipping, info):
        return shipping.street

    def resolve_house_number(shipping: Shipping, info):
        return shipping.house_number
