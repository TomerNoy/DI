import datetime
import random
from django.utils import timezone
import os
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
django.setup()

from rent.models import *

fake = Faker()

scooter = VehicleType.objects.create(name='scooter')
bike = VehicleType.objects.create(name='bike')
car = VehicleType.objects.create(name='car')
truck = VehicleType.objects.create(name='truck')
jetpack = VehicleType.objects.create(name='jetpack')

small = VehicleSize.objects.create(name='small')
medium = VehicleSize.objects.create(name='medium')
big = VehicleSize.objects.create(name='big')

all_vehicle_types = list(VehicleType.objects.all())
all_vehicle_sizes = list(VehicleSize.objects.all())

# auto generate all vehicle rates solution (not realistic but consistent)
for vehicle_type in all_vehicle_types:
    for vehicle_size in all_vehicle_sizes:
        vehicle_type_grade = all_vehicle_types.index(vehicle_type) + 6
        vehicle_size_grade = all_vehicle_sizes.index(vehicle_size) + 6
        daily_rate = vehicle_type_grade * vehicle_size_grade
        RentalRate.objects.create(daily_rate=daily_rate, vehicle_type=vehicle_type, vehicle_size=vehicle_size)

for p in range(100):
    person = Customer.objects.create(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        phone_number=fake.phone_number(),
        address=fake.address(),
        city=fake.city(),
        country=fake.country())

# auto generate all vehicle real cost solution (not realistic but consistent)
for i in range(80):
    vehicle_type = random.choice(list(all_vehicle_types))
    size = random.choice(list(all_vehicle_sizes))
    date_created = fake.date_time_between(datetime.datetime(2000, 1, 1), timezone.now())
    vehicle_type_grade = all_vehicle_types.index(vehicle_type) + 55
    vehicle_size_grade = all_vehicle_sizes.index(size) + 55
    real_cost = vehicle_type_grade * vehicle_size_grade
    Vehicle.objects.create(
        vehicle_type=vehicle_type,
        size=size,
        date_created=date_created,
        real_cost=real_cost,
    )

for r in range(100):
    customer = random.choice(Customer.objects.all())

    # we need to get avail random vehicle
    # so we loop through all avail vehicles randomly while excluding already checked ones
    vehicle_list = list(Vehicle.objects.all())

    vehicle = ''

    while len(vehicle_list) > 0:
        random_vehicle = random.choice(vehicle_list)
        vehicle_list.remove(random_vehicle)

        # if vehicle in not linked to a rent where it's not returned yet
        if len(random_vehicle.rental_set.filter(return_date=None)) == 0:
            vehicle = random_vehicle
            break

    if vehicle == '':
        # no vehicles avail
        print('no vehicle avail for rent, create more?')
        break

    rental_date = fake.date_time_between(vehicle.date_created, timezone.now())
    return_date = fake.date_time_between(rental_date, timezone.now())
    return_dates = [return_date, None]

    Rental.objects.create(
        rental_date=rental_date,  # random past
        return_date=random.choice(return_dates),  # random past after {rental_date}
        customer=customer,
        vehicle=vehicle,
    )
