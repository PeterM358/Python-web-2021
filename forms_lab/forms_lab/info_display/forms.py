from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator


def name_validation(value):
    if not value[0] == value[0].upper():
        raise ValidationError('The name must start with an uppercase letter')


def age_validation(value):
    if value < 0:
        raise ValidationError('The age cannot be less than zero')


def password_validation(value):
    if any([not x.isalnum() for x in value]):
        raise ValidationError('Enter valid password')


class DisplayInfo(forms.Form):
    name = forms.CharField(
        validators=[
            name_validation,
            MinLengthValidator(6)
        ]
    )
    age = forms.IntegerField(
        widget=forms.NumberInput,
        validators=[
            age_validation,
        ]
    )
    email = forms.EmailField(
        widget=forms.EmailInput
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        validators=[
            password_validation,
            MinLengthValidator(8),
        ]
    )
    text = forms.CharField(
        widget=forms.Textarea
    )
