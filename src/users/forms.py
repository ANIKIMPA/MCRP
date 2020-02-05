from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import LoginLevel


class LoginLevelCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = LoginLevel
        fields = ('email',)


class LoginLevelChangeForm(UserChangeForm):

    class Meta:
        model = LoginLevel
        fields = ('email',)