from django import forms
from django.db.models import fields
from . models import *

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']