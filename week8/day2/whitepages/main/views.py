from django.shortcuts import render
from .models import Person


def find_person(request, input):

    if any(char.isdigit() for char in input):
        person = Person.objects.filter(phone=input)
    else:
        person = Person.objects.filter(name=input)
    if not person:
        person = None
    else:
        person = person[0]
    return render(request, 'whitepages.html', {'person': person})
