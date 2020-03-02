from django.db import models
from django.utils.timezone import now
from users.models import LoginLevel

# Create your models here.


class BomFile(models.Model):
    title = models.CharField(max_length=50, default="Untitled")
    number_of_items = models.PositiveIntegerField(blank=True, default=1)
    owner = models.ForeignKey(LoginLevel, related_name='bom_files', on_delete=models.CASCADE, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date', 'title']
        verbose_name = 'BomFile'
        verbose_name_plural = 'BomFiles'

    def __str__(self):
        return self.title


class BomItem(models.Model):
    part_number = models.CharField(max_length=12, blank=True, null=True)
    tipo = models.CharField(max_length=20, blank=True, null=True)
    parent = models.CharField(max_length=12, blank=True, null=True)
    qty = models.PositiveIntegerField(blank=True, default=1)
    file = models.ForeignKey(BomFile, related_name='bom_items', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'BomItem'
        verbose_name_plural = 'BomItems'

    def __str__(self):
        return self.part_number

class MastFile(models.Model):
    title = models.CharField(max_length=50, default="Untitled")
    number_of_items = models.PositiveIntegerField(blank=True, default=1)
    planning_horizon_length = models.PositiveIntegerField(blank=True, default=0)
    number_time_buckets = models.PositiveIntegerField(blank=True, default=0)
    owner = models.ForeignKey(LoginLevel, related_name='mast_files', on_delete=models.CASCADE, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date', 'title']
        verbose_name = 'MastFile'
        verbose_name_plural = 'MastFiles'

    def __str__(self):
        return self.title


class Period(models.Model):
    part_number = models.CharField(max_length=12, blank=True, null=True)
    data = models.PositiveIntegerField(blank=True, null=True)
    order = models.PositiveIntegerField(blank=True, null=True)
    file = models.ForeignKey(MastFile, related_name='periods', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['file', 'part_number', 'order']
        verbose_name = 'Period'
        verbose_name_plural = 'Periods'
        unique_together = ("file", "part_number", "order",)

    def __str__(self):
        return f"File: {self.file}, Part Number: {self.part_number}, Period {self.order}: {self.data}"


class InvFile(models.Model):
    title = models.CharField(max_length=50, default="Untitled")
    number_of_items = models.PositiveIntegerField(blank=True, default=1)
    lead_time = models.PositiveIntegerField(blank=True, default=0)
    number_of_periods = models.PositiveIntegerField(blank=True, default=0)
    annual_carrying = models.PositiveIntegerField(blank=True, default=0)
    owner = models.ForeignKey(LoginLevel, related_name='inv_files', on_delete=models.CASCADE, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date', 'title']
        verbose_name = 'InvFile'
        verbose_name_plural = 'InvFiles'

    def __str__(self):
        return self.title


class InvItem(models.Model):
    part_number = models.CharField(max_length=12, blank=True, null=True)
    safe_stock = models.PositiveIntegerField(blank=True, null=True)
    on_hand = models.PositiveIntegerField(blank=True, null=True)
    past_due = models.PositiveIntegerField(blank=True, null=True)
    receipts = models.CharField(max_length=250, blank=True, null=True)
    file = models.ForeignKey(InvFile, related_name='inv_items', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['file', 'id']
        verbose_name = 'InvItem'
        verbose_name_plural = 'InvItems'

    def __str__(self):
        return f"File: {self.file}, Part Number: {self.part_number}"

class ItemMasterFile(models.Model):
    title = models.CharField(max_length=50, default="Untitled")
    number_of_items = models.PositiveIntegerField(blank=True, default=1)
    owner = models.ForeignKey(LoginLevel, related_name='item_master_files', on_delete=models.CASCADE, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date', 'title']
        verbose_name = 'ItemMasterFile'
        verbose_name_plural = 'ItemMasterFiles'

    def __str__(self):
        return self.title


class ItemMaster(models.Model):
    part_number = models.CharField(max_length=12, blank=True, null=True)
    clase = models.CharField(max_length=50, blank=True, null=True)
    lot_size = models.CharField(max_length=50, blank=True, null=True)
    multiple = models.PositiveIntegerField(blank=True, null=True)
    lead_time = models.PositiveIntegerField(blank=True, null=True)
    scrap_percent = models.PositiveIntegerField(blank=True, null=True)
    unit_value = models.PositiveIntegerField(blank=True, null=True)
    order_cost = models.PositiveIntegerField(blank=True, null=True)
    demand = models.PositiveIntegerField(blank=True, null=True)
    file = models.ForeignKey(ItemMasterFile, related_name='inv_items', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['file', 'id']
        verbose_name = 'ItemMaster'
        verbose_name_plural = 'ItemMasters'

    def __str__(self):
        return f"File: {self.file}, Part Number: {self.part_number}"


