from django import forms

from classapp.models import Person


# Formularz modelu
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
