from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Usuario


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)

    class Meta(UserCreationForm):
        model = Usuario
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')


class UsuarioChangeForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = ('email',)