from django.shortcuts import render

from data import people

people_by_age = sorted(people, key=lambda item: item['age'])


def people(request):
    return render(request, 'people.html', context={'people': people_by_age})


def person(request, id):
    for person in people_by_age:
        if person['id'] == int(id):
            return render(request, 'person.html', context={'person': person})

    return render(request, 'person.html', context={'person': {}})
