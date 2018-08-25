from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    # international format (+380123456789)
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
