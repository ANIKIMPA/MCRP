from rest_framework import serializers
from .models import Item, File, Period


class FileSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Item.objects.all(), required=False)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = File
        fields = ('id', 'owner', 'title', 'tipo', 'items')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'part_number', 'tipo', 'parent', 'qty', 'file')


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ('id', 'part_number', 'order', 'file')
