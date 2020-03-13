from .models import Usuario
from rest_framework import serializers
from mrp.models import BomFile, MastFile, InvFile, ItemMasterFile


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    bom_files = serializers.PrimaryKeyRelatedField( required=False,
        many=True, queryset=BomFile.objects.all())

    mast_files = serializers.PrimaryKeyRelatedField( required=False,
        many=True, queryset=MastFile.objects.all())

    inv_files = serializers.PrimaryKeyRelatedField( required=False,
        many=True, queryset=InvFile.objects.all())

    item_master_files = serializers.PrimaryKeyRelatedField( required=False,
        many=True, queryset=ItemMasterFile.objects.all())

    class Meta:
        model = Usuario
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'is_staff', 'is_active', 'bom_files',
            'mast_files', 'inv_files', 'item_master_files']
