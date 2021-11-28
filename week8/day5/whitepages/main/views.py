from django.shortcuts import render, redirect
from .models import Person


def person(request, pk):
    _person = Person.objects.get(pk=pk)
    context = {'person': _person}
    return render(request, 'person.html', context)


def search_person_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('phone_number')

        _person = ''

        if name:
            try:
                _person = Person.objects.get(name=name.title())
            except Person.DoesNotExist:
                return render(request, '404.html')

        elif number:
            try:
                _person = Person.objects.get(phone_number=number)
            except Person.DoesNotExist:
                return render(request, '404.html')

        print('person', number)
        if _person == '':
            return render(request, '404.html')

        context = {'person': _person}
        return render(request, 'person.html', context)

    if request.method == 'GET':
        return render(request, 'search.html')


def home(request):
    persons = Person.objects.all()
    print(persons)
    context = {'persons': persons}
    return render(request, 'home.html', context)
