from django import forms
from .models import Category


class TodoForm(forms.Form):
    title = forms.CharField(max_length=10)
    details = forms.CharField(widget=forms.Textarea)
    deadline_date = forms.DateTimeField(widget=forms.SelectDateWidget())
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    field_order = ['title', 'details', 'deadline_date', 'category']
