from django.shortcuts import render
from .models import Animal, Family


def family(request, family_id):
    family = Family.objects.get(id=family_id)
    animals = Animal.objects.filter(family_id=family)
    return render(request, 'family.html', {'family': family.name, 'animals': animals})


def animal(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    return render(request, 'animal.html', {'animal': animal})


def animals(request):
    animals = Animal.objects.all()
    return render(request, 'animals.html', {'animals': animals})
