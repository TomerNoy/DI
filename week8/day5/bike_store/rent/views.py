from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *
from datetime import datetime


def rentals_view(request):
    rentals = Rental.objects.all().order_by('return_date')
    context = {'rentals': rentals}
    return render(request, 'rentals_view.html', context)


def rental_view(request, pk):
    rental = Rental.objects.get(pk=pk)

    context = {'rental': rental}
    return render(request, 'rental_view.html', context)


# def rental_form_view(request):
#     if request.method == 'POST':
#         # check if customer and vehicle exist if not return err
#         vehicle_id = request.POST.get('vehicle_ID')
#         customer_id = request.POST.get('customer_ID')
#         vehicle = get_object_or_404(Vehicle, id=vehicle_id)
#         customer = get_object_or_404(Customer, id=customer_id)
#
#         # in order to check if vehicle returned we need:
#         # 1. list records of rentals
#         rentals = customer.rental_set.filter(customer=customer, vehicle=vehicle)
#
#         # 2. check if at least 1 has unreturned
#         # (by design if such exists we'll only get one)
#         for rental in rentals:
#             print(rental.return_date)
#             if not rental.return_date:
#                 return HttpResponse('Sorry, not returned yet!\npress back and try again?', content_type='text/plain')
#
#         rental = Rental.objects.create(rental_date=datetime.now(), customer=customer, vehicle=vehicle)
#         # success -> send user to rental view
#         return redirect('rental_view', rental.pk)
#
#     if request.method == 'GET':
#         return render(request, 'rental_form_view.html')


def rental_form_view(request):
    if request.method == 'POST':
        # print(request.POST)
        form = RentalForm(request.POST)

        if form.is_valid():
            vehicle_id = request.POST.get('vehicle')
            customer_id = request.POST.get('customer')

            # print('-->', vehicle_id, customer_id)
            vehicle = get_object_or_404(Vehicle, id=vehicle_id)
            customer = get_object_or_404(Customer, id=customer_id)

            # in order to check if vehicle returned we need:
            # 1. list records of rentals
            rentals = customer.rental_set.filter(customer=customer, vehicle=vehicle)

            # 2. check if at least 1 has unreturned
            # (by design if such exists we'll only get one)
            for rental in rentals:
                # print(rental.return_date)
                if not rental.return_date:
                    return HttpResponse('Sorry, not returned yet!\npress back and try again?',
                                        content_type='text/plain')

            rental = Rental.objects.create(rental_date=datetime.now(), customer=customer, vehicle=vehicle)
            # success -> send user to rental view
            return redirect('rental_view', rental.pk)

    if request.method == 'GET':
        form = RentalForm()
    return render(request, 'rental_form_view.html', {'form': form})


def customers_view(request):
    customers = Customer.objects.all().order_by('first_name')
    context = {'customers': customers}
    return render(request, 'customers_view.html', context)


def customer_view(request, pk):
    customer = Customer.objects.get(pk=pk)

    context = {'customer': customer}
    return render(request, 'customer_view.html', context)


# def customer_form_view(request):
#     return render(request, 'customer_form_view.html')


def customer_form_view(request):
    if request.method == 'POST':
        # print(request.POST)
        form = CustomerForm(request.POST)

        if form.is_valid():
            # print(form.cleaned_data)
            customer = Customer.objects.create(**form.cleaned_data)
            return redirect('customer_view', customer.pk)

    if request.method == 'GET':

        form = CustomerForm()
        # print('--->', form)
    return render(request, 'customer_form_view.html', {'form': form})


def vehicles_view(request):
    types = list(VehicleType.objects.all())

    vehicles_group_by_type = {}
    for _type in types:
        group = Vehicle.objects.filter(vehicle_type=_type.pk)
        vehicles_group_by_type[_type.name] = group

    context = {'vehicles_group_by_type': vehicles_group_by_type}
    return render(request, 'vehicles_view.html', context)


def vehicle_view(request, pk):
    vehicle = Vehicle.objects.get(pk=pk)
    context = {'vehicle': vehicle}
    return render(request, 'vehicle_view.html', context)


def vehicle_form_view(request):
    if request.method == 'POST':
        # print(request.POST)
        form = VehicleForm(request.POST)

        if form.is_valid():
            # print(form.cleaned_data)
            vehicle = Vehicle.objects.create(**form.cleaned_data)
            return redirect('vehicle_view', vehicle.pk)

    if request.method == 'GET':
        form = VehicleForm()
        # print('--->', form)
    return render(request, 'vehicle_form_view.html', {'form': form})
