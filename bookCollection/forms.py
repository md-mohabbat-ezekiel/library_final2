from django import forms
from . import models

class AddCarForm(forms.ModelForm):
    class Meta:
        model = models.AddBook
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['name', 'email', 'body']