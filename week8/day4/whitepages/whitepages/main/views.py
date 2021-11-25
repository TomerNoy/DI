from django.shortcuts import render, redirect
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


def homepage(request):
    persons = Person.objects.all()
    return render(request, 'home.html', {'persons': persons})


def find_person_form(request):
    print('here')
    if request.method == 'POST':
        input = request.POST['input']
        return redirect('person_select', input)

    if request.method == 'GET':
        return render(request, 'find_person.html')
