import os
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whitepages.settings')
django.setup()

from main.models import *

fake = Faker()

for i in range(100):
    Person.objects.create(
        name=fake.name(),
        email=fake.email(),
        phone_number=fake.phone_number(),
        address=fake.address()
    )
