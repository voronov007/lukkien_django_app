from ...models import Shipping


def resolve_all_shippings(root, info):
    return Shipping.objects.all()
