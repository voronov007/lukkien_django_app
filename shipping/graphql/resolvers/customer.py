from ...models import Customer


def resolve_all_customers(root, info):
    return Customer.objects.all()
