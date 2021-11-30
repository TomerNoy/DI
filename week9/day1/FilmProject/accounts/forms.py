from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User


class MyAuthenticationForm(AuthenticationForm):
    pass
    # date = forms.DateTimeField(initial=timezone.now())
    # field_order = ['date', 'password', 'username']


class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

# this is example from class
# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = User

#         fields = ['username', 'first_name', 'last_name', 'email']
