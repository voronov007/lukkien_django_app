from django.db import models

from .person import Person


class Shipping(Person):
    postal_code = models.CharField(max_length=30)  # can have letters
    city = models.CharField(max_length=40)
    street = models.CharField(max_length=50)
    house_number = models.CharField(max_length=10)  # 11b is possible

    class Meta:
        unique_together = ("postal_code", "street", "house_number")
