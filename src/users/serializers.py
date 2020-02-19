from .models import LoginLevel
from rest_framework import serializers
from mrp.models import BomFile, MastFile


class LoginLevelSerializer(serializers.HyperlinkedModelSerializer):
    bom_files = serializers.PrimaryKeyRelatedField( required=False,
        many=True, queryset=BomFile.objects.all())

    mast_files = serializers.PrimaryKeyRelatedField( required=False,
        many=True, queryset=MastFile.objects.all())

    class Meta:
        model = LoginLevel
        fields = ['id', 'username', 'email', 'bom_files', 'mast_files']
