from .models import LoginLevel
from rest_framework import serializers

class LoginLevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LoginLevel
        fields = "__all__"