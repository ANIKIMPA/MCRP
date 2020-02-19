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
        ordering = ['title']
        verbose_name = 'BomFile'
        verbose_name_plural = 'BomFiles'

    def __str__(self):
        return self.title


class Item(models.Model):
    part_number = models.CharField(max_length=12, blank=True, null=True)
    tipo = models.CharField(max_length=20, blank=True, null=True)
    parent = models.CharField(max_length=12, blank=True, null=True)
    qty = models.PositiveIntegerField(blank=True, default=1)
    file = models.ForeignKey(BomFile, related_name='items', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['part_number']
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

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
        ordering = ['title']
        verbose_name = 'MastFile'
        verbose_name_plural = 'MastFiles'

    def __str__(self):
        return self.title


class Period(models.Model):
    part_number = models.CharField(max_length=12, blank=True, null=True)
    data = models.CharField(max_length=20, blank=True, null=True)
    order = models.PositiveIntegerField(blank=True, null=True)
    file = models.ForeignKey(MastFile, related_name='periods', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['file', 'part_number', 'order']
        verbose_name = 'Master Schedule'
        verbose_name_plural = 'Masters Schedules'

    def __str__(self):
        return f"File: {self.file}, Part Number: {self.part_number}, Period {self.order}: {self.data}"
