from rest_framework import serializers
from .models import (
    BomFile, BomItem, MastFile, Period, InvFile, InvItem, ItemMasterFile, ItemMaster
)


class BomFileSerializer(serializers.ModelSerializer):
    bom_items = serializers.PrimaryKeyRelatedField(many=True, queryset=BomItem.objects.all(), required=False)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = BomFile
        fields = ('id', 'owner', 'title', 'number_of_items', 'bom_items', 'created_date')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BomItem
        fields = ('id', 'part_number', 'tipo', 'parent', 'qty', 'file')


class MastFileSerializer(serializers.ModelSerializer):
    periods = serializers.PrimaryKeyRelatedField(many=True, queryset=Period.objects.all(), required=False)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = MastFile
        fields = ('id', 'owner', 'title', 'periods', 'created_date',
                  'number_of_items', 'planning_horizon_length', 'number_time_buckets')


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ('id', 'part_number', 'data', 'order', 'file')

class InvFileSerializer(serializers.ModelSerializer):
    inv_items = serializers.PrimaryKeyRelatedField(many=True, queryset=InvItem.objects.all(), required=False)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = InvFile
        fields = ('id', 'owner', 'title', 'inv_items', 'created_date',
                  'number_of_items', 'lead_time', 'number_of_periods', 'annual_carrying')


class InvItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvItem
        fields = ('id', 'part_number', 'safe_stock', 'on_hand', 'past_due', 'receipts', 'file')

class ItemMasterFileSerializer(serializers.ModelSerializer):
    items_masters = serializers.PrimaryKeyRelatedField(many=True, queryset=ItemMaster.objects.all(), required=False)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ItemMasterFile
        fields = ('id', 'owner', 'title', 'items_masters', 'created_date', 'number_of_items')


class ItemMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMaster
        fields = ('id', 'part_number', 'clase', 'lot_size', 'multiple', 'lead_time', 'yield_percent',
            'unit_value', 'order_cost', 'carrying_cost', 'demand', 'file')
