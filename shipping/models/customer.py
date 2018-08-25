from django.db import models

from .person import Person


class Customer(Person):
    date_of_birth = models.DateField()
