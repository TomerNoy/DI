from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy

from accounts.forms import MyAuthenticationForm, UserForm, RegistrationForm
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from films.models import Film


class MySignupView(CreateView):
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class ProfileView(CreateView):
    success_url = reverse_lazy('profile')
    template_name = 'accounts/profile.html'


class DaLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = MyAuthenticationForm

    def get_success_url(self):
        return reverse_lazy('profile')


# @login_required
# def test_page(request):
#     return render(request, 'accounts/login.html')

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')


# this is example from class
# class SignupView(CreateView):
#     form_class = RegistrationForm
#     success_url = reverse_lazy('homepage')
#     template_name = 'accounts/signup.html'
