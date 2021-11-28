from django import forms
from phonenumber_field.modelfields import PhoneNumberField

# from django.core.validators import EmailValidator

from rent.models import VehicleType, VehicleSize, Customer, Vehicle


class CustomerForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=60)
    # phone_number = PhoneNumberField(max_length=30)  # todo: this doesn't show!?
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=30)
    country = forms.CharField(max_length=30)

    first_name.widget.attrs.update({'class': 'form-control'})
    last_name.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    # phone_number.widget.attrs.update({'class': 'form-control'})  # todo: this throws an err
    address.widget.attrs.update({'class': 'form-control'})
    city.widget.attrs.update({'class': 'form-control'})
    country.widget.attrs.update({'class': 'form-control'})

    field_order = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'city', 'country']


class VehicleForm(forms.Form):
    # todo dropdown for add forms !!!
    vehicle_type = forms.ModelChoiceField(queryset=VehicleType.objects.all())
    date_created = forms.DateTimeField()
    real_cost = forms.DecimalField(max_digits=10, decimal_places=2)
    size = forms.ModelChoiceField(queryset=VehicleSize.objects.all())

    vehicle_type.widget.attrs.update({'class': 'form-control'})
    date_created.widget.attrs.update({'class': 'form-control'})
    real_cost.widget.attrs.update({'class': 'form-control'})
    size.widget.attrs.update({'class': 'form-control'})

    field_order = ['vehicle_type', 'date_created', 'real_cost', 'size']


class RentalForm(forms.Form):
    # rental_date = forms.DateTimeField()
    # return_date = forms.DateTimeField()
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    vehicle = forms.ModelChoiceField(queryset=Vehicle.objects.all())

    # rental_date.widget.attrs.update({'class': 'form-control'})
    # return_date.widget.attrs.update({'class': 'form-control'})
    customer.widget.attrs.update({'class': 'form-control'})
    vehicle.widget.attrs.update({'class': 'form-control'})

    field_order = ['rental_date', 'return_date', 'customer', 'vehicle']
