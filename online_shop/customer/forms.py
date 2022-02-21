from django import forms


class ContactForm(forms.Form):
    name: forms.CharField( max_length=30, required=True)
    emial : forms.EmailField(required=True)
    comment: forms.CharField(max_length=255, required=False)

    def __str__(self):
        return f"user:{self.name} says:\n{self.comment}"