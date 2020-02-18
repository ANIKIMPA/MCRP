from .models import LoginLevel
from rest_framework import serializers
from mrp.models import File


class LoginLevelSerializer(serializers.HyperlinkedModelSerializer):
    files = serializers.PrimaryKeyRelatedField(
        many=True, queryset=File.objects.all())

    class Meta:
        model = LoginLevel
        fields = ['id', 'username', 'email', 'files']
