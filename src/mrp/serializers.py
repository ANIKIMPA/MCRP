from rest_framework import serializers
from .models import (
    BomFile, BomItem, MastFile, MastItem, InvFile, InvItem,
    ItemMasterFile, ItemMaster, Report, ReportItem, ReportPeriod
)


class BomFileSerializer(serializers.ModelSerializer):
    bom_items = serializers.PrimaryKeyRelatedField(many=True, queryset=BomItem.objects.all(), required=False)
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = BomFile
        fields = ('id', 'owner', 'title', 'number_of_items', 'bom_items', 'created_date', 'removed')


class BomItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BomItem
        fields = ('id', 'part_number', 'tipo', 'parent', 'qty', 'file')


class MastFileSerializer(serializers.ModelSerializer):
    mast_items = serializers.PrimaryKeyRelatedField(many=True, queryset=MastItem.objects.all(), required=False)
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = MastFile
        fields = ('id', 'owner', 'title', 'mast_items', 'created_date',
                  'number_of_items', 'planning_horizon_length', 'number_time_buckets', 'removed')


class MastItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MastItem
        fields = ('id', 'part_number', 'periods', 'order', 'file')

class InvFileSerializer(serializers.ModelSerializer):
    inv_items = serializers.PrimaryKeyRelatedField(many=True, queryset=InvItem.objects.all(), required=False)
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = InvFile
        fields = ('id', 'owner', 'title', 'inv_items', 'created_date',
                  'number_of_items', 'lead_time', 'number_of_periods', 'annual_carrying', 'removed')


class InvItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvItem
        fields = ('id', 'part_number', 'safe_stock', 'on_hand', 'past_due', 'receipts', 'order', 'file')

class ItemMasterFileSerializer(serializers.ModelSerializer):
    items_masters = serializers.PrimaryKeyRelatedField(many=True, queryset=ItemMaster.objects.all(), required=False)
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = ItemMasterFile
        fields = ('id', 'owner', 'title', 'items_masters', 'created_date', 'number_of_items', 'removed')


class ItemMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMaster
        fields = ('id', 'part_number', 'clase', 'lot_size', 'multiple', 'lead_time', 'yield_percent',
            'unit_value', 'order_cost', 'carrying_cost', 'demand', 'order', 'file')


class ReportPeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportPeriod
        fields = ('period', 'gross_requirement', 'receipt', 'on_hand',
            'net_requirement')


class ReportItemSerializer(serializers.ModelSerializer):
    periods = ReportPeriodSerializer(many=True)
    
    class Meta:
        model = ReportItem
        fields = ('part_number', 'yield_percent', 'lead_time', 'order_cost',
            'parent', 'carrying_cost', 'qty', 'lot_size', 'safe_stock', 'factor',
            'on_hand', 'periods', 'order')
        
    def create(self, validated_data):
        item_validated_data = validated_data.pop('periods')
        item = ReportItem.objects.create(**validated_data)
        serializer = self.fields['periods']
        for each in item_validated_data:
            each['item'] = item
        periods = serializer.create(item_validated_data)
        return item

class ReportSerializer(serializers.ModelSerializer):
    items = ReportItemSerializer(many=True)

    class Meta:
        model = Report
        fields = ('id', 'title', 'items')
    
    def create(self, validated_data):
        report_validated_data = validated_data.pop('items')
        report = Report.objects.create(**validated_data)
        reportSerializer = self.fields['items']
        for each in report_validated_data:
            each['report'] = report
        items = reportSerializer.create(report_validated_data)
        return report

