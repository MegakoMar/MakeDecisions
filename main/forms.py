from .models import User
from django.forms import ModelForm, fields, TextInput, Select


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'groups']

        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'type': 'email'
            }),
            "groups": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Должность'
            }),
         }
            