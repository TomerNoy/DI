import os
from builtins import id

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FilmProject.settings')
django.setup()

from films.models import *

categories = ['Action', 'Drama', 'Comedy', ]

for category in categories:
    Category.objects.create(name=category)

countries = ['Australia', 'Israel', 'Canada', 'United States']

for country in countries:
    Country.objects.create(name=country)

directors = [
    {'fname': 'ALFRED', 'lname': 'HITCHCOCK'},
    {'fname': 'JOHN', 'lname': 'FORD'},
    {'fname': 'INGMAR', 'lname': 'BERGMAN'},
]

for director in directors:
    Director.objects.create(first_name=director['fname'], last_name=director['lname'])
