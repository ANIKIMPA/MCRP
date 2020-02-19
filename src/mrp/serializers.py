from rest_framework import serializers
from .models import BomFile, Item, MastFile, Period


class BomFileSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(many=True, queryset=Item.objects.all(), required=False)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = BomFile
        fields = ('id', 'owner', 'title', 'number_of_items', 'items')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'part_number', 'tipo', 'parent', 'qty', 'file')


class MastFileSerializer(serializers.ModelSerializer):
    periods = serializers.PrimaryKeyRelatedField(many=True, queryset=Period.objects.all(), required=False)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = MastFile
        fields = ('id', 'owner', 'title', 'periods',
                  'number_of_items', 'planning_horizon_length', 'number_time_buckets')


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ('id', 'part_number', 'data', 'order', 'file')
