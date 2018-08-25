import pytest
from graphene.test import Client

from api.graphql.schema import Schema as graphql_schema
from ..models import Customer, Shipping

pytestmark = pytest.mark.django_db


def test_get_all_customers_ok():
    customer = Customer.objects.create(
        first_name="Ali", last_name="Baba",
        phone_number="+88991234567", email="example@gmail.com",
        date_of_birth="1983-12-01"
    )
    client = Client(graphql_schema)
    query = """
        query {
          customers {
            id
            firstName
            lastName
            phoneNumber
            email
            dateOfBirth
          }
        }
    """
    executed = client.execute(query)

    customers_data = executed['data']['customers']
    assert len(customers_data) == 1
    assert customers_data[0]['phoneNumber'] == customer.phone_number
    assert customers_data[0]['email'] == customer.email


def test_get_all_shippings_ok():
    shipping = Shipping.objects.create(
        first_name="Ali", last_name="Baba",
        phone_number="+88991234567", email="example@gmail.com",
        postal_code="97Y9A", city="Amsterdam", street="Example street",
        house_number="19A"
    )
    client = Client(graphql_schema)
    query = """
        query {
          shippings {
            id
            firstName
            lastName
            phoneNumber
            email
            postalCode
            city
            street
            houseNumber
          }
        }
    """
    executed = client.execute(query)

    shippings_data = executed['data']['shippings']
    assert len(shippings_data) == 1
    assert shippings_data[0]['phoneNumber'] == shipping.phone_number
    assert shippings_data[0]['email'] == shipping.email
    assert shippings_data[0]['postalCode'] == shipping.postal_code
    assert shippings_data[0]['city'] == shipping.city
