from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import User

class ContactForm(forms.Form):
    name: forms.CharField( max_length=30, required=True)
    emial : forms.EmailField(required=True)
    comment: forms.CharField(max_length=255, required=False)

    def __str__(self):
        return f"user:{self.name} says:\n{self.comment}"

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "phone", "password1", "password2"]
