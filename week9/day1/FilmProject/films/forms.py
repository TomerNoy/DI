from django import forms
from .models import *
from django.forms import ModelForm, Select


# class PostForm(forms.Form):
#     title = forms.CharField(max_length=200)
#     content = forms.TextField()
#     image = forms.ImageField(upload_to='post_pictures/')
#     author = forms.CharField(max_length=60)
#     timestamp = forms.DateTimeField(auto_now_add=True)


class AddFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
        labels = {
            'created_in_country': 'Country'
        }


class AddDirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
