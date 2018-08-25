import graphene

from .person import PersonType
from ...models import Customer


class CustomerType(PersonType):
    date_of_birth = graphene.types.datetime.Date()

    def resolve_date_of_birth(customer: Customer, info):
        return customer.date_of_birth
