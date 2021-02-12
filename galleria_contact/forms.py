from django import forms
from django.core import validators


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(200, 'Name can not be more than 200 characters')
        ]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(200, 'Email can not be more than 200 characters')
        ]
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(200, 'subject can not be more than 200 characters')
        ]
    )
    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Name', 'class': 'form-control'})
    )
