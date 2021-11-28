from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)
    phone_number = PhoneNumberField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class VehicleType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class VehicleSize(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    date_created = models.DateTimeField()
    real_cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.size.name} {self.vehicle_type.name} {self.date_created.year}'


class Rental(models.Model):
    rental_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


class RentalRate(models.Model):
    daily_rate = models.DecimalField(max_digits=5, decimal_places=2)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.vehicle_type.name + ' ' + str(self.daily_rate)
