from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    # international format
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"""
        {type(self).__name__}({self.first_name} {self.last_name})
        """

    def __repr__(self):
        return self.__str__()


class Customer(Person):
    date_of_birth = models.DateField()


class Shipping(Person):
    postal_code = models.CharField(max_length=30)  # can have letters
    city = models.CharField(max_length=40)
    street = models.CharField(max_length=50)
    house_number = models.CharField(max_length=10)  # 11b is possible

    class Meta:
        unique_together = ("postal_code", "street", "house_number")
