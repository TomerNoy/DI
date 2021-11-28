from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30, unique=True)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=60)

    def __str__(self):
        return self.name + ' ' + str(self.phone_number)
