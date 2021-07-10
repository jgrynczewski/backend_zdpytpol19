from django import forms

from form.models import Message

# Formularz Django
class ContactForm(forms.Form):
    CHOICES = [
        ("question", "Pytanie"),
        ("other", "Inne")
    ]

    name = forms.CharField(label="Imię")
    email = forms.EmailField(label="Email")
    category = forms.ChoiceField(choices=CHOICES, label="Kategoria")
    subject = forms.CharField(label="Tytuł")
    body = forms.CharField(widget=forms.Textarea, label="Treść")


# Formularz modelu
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        labels = {
            "name": "Imię",
            "email": "Email",
            "category": "Kategoria",
            "subject": "Tytuł",
            "body": "Treść"
        }