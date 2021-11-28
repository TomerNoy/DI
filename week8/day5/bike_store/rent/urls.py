from django.urls import path
from . import views

urlpatterns = [
    path('rental/', views.rentals_view, name='rentals_view'),
    path('rental/<pk>', views.rental_view, name='rental_view'),
    path('rental/add/', views.rental_form_view, name='rental_form_view'),

    path('customer/', views.customers_view, name='customers_view'),
    path('customer/<pk>', views.customer_view, name='customer_view'),
    path('customer/add/', views.customer_form_view, name='customer_form_view'),

    path('vehicle/', views.vehicles_view, name='vehicles_view'),
    path('vehicle/<pk>', views.vehicle_view, name='vehicle_view'),
    path('vehicle/add/', views.vehicle_form_view, name='vehicle_form_view'),
]
