import graphene

from shipping.graphql.schema import ShippingQuery


class Query(ShippingQuery, graphene.ObjectType):
    pass


Schema = graphene.Schema(query=Query)
