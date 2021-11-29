from django import forms
from .models import *


# class TodoForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     details = forms.CharField(widget=forms.Textarea)
#     deadline_date = forms.DateTimeField(widget=forms.SelectDateWidget())
#     category = forms.ModelChoiceField(queryset=Category.objects.all())
#     field_order = ['title', 'details', 'deadline_date', 'category']


class AddTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'details': forms.Textarea(attrs={'class': 'textarea'}),
        }
