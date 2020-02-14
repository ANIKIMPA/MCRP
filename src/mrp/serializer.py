from .models import Item, File
from rest_framework import serializers

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'title', 'tipo')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'part_number', 'tipo', 'parent', 'qty', 'file')
