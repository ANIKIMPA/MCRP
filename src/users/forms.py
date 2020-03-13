from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Usuario


class RegistrationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Usuario
        fields = ('email', 'password1', 'password2')


class UsuarioChangeForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = ('email',)