from .models import *
from django import forms

class add_new_form(forms.ModelForm):
    class Meta:
        model =  movie_data
        fields = "__all__"