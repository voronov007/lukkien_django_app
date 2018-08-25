import graphene

from ...models import Person


class PersonType(graphene.ObjectType):
    id = graphene.Int()
    first_name = graphene.String()
    last_name = graphene.String()
    phone_number = graphene.String()
    email = graphene.String()

    def resolve_id(person: Person, info):
        return person.pk

    def resolver_first_name(person: Person, info):
        return person.first_name

    def resolve_last_name(person: Person, info):
        return person.last_name

    def resolve_phone_number(person: Person, info):
        return person.phone_number

    def resolve_email(person: Person, info):
        return person.email
