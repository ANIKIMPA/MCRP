from django.db import models
from datetime import datetime
from users.models import Usuario
from django.core.validators import MaxValueValidator, MinValueValidator

# Model for Bill of Material File.
class BomFile(models.Model):
    title = models.CharField(max_length=50, default="Untitled")
    number_of_items = models.PositiveIntegerField(blank=True, default=1)
    owner = models.ForeignKey(Usuario, related_name='bom_files', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    removed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date', 'title']
        verbose_name = 'BomFile'
        verbose_name_plural = 'BomFiles'

    def __str__(self):
        return self.title

# Model for Bill of Material item.
class BomItem(models.Model):
    part_number = models.CharField(max_length=12)
    tipo = models.CharField(max_length=20, default="MAT")
    parent = models.CharField(max_length=12, blank=True, null=True)
    qty = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0)])
    file = models.ForeignKey(BomFile, related_name='bom_items', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_date = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['file', 'id']
        verbose_name = 'BomItem'
        verbose_name_plural = 'BomItems'

    def __str__(self):
        return self.part_number

# Model for Master Schedule file.
class MastFile(models.Model):
    title = models.CharField(max_length=50, default="Untitled")
    number_of_items = models.PositiveIntegerField(blank=True, default=1)
    planning_horizon_length = models.PositiveIntegerField(blank=True, default=0)
    number_time_buckets = models.PositiveIntegerField(blank=True, default=0)
    owner = models.ForeignKey(Usuario, related_name='mast_files', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    removed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date', 'title']
        verbose_name = 'MastFile'
        verbose_name_plural = 'MastFiles'

    def __str__(self):
        return self.title


# Model for Master Schedule item.
class MastItem(models.Model):
    part_number = models.CharField(max_length=12)
    periods = models.CharField(max_length=250, blank=True, null=True)
    order = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    file = models.ForeignKey(MastFile, related_name='mast_items', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_date = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['file', 'order']
        verbose_name = 'MastItem'
        verbose_name_plural = 'MastItems'

    def __str__(self):
        return f"File: {self.file}, Part Number: {self.part_number}"


# Model for Inventory Status file.
class InvFile(models.Model):
    title = models.CharField(max_length=50, default="Untitled")
    number_of_items = models.PositiveIntegerField(blank=True, default=1)
    lead_time = models.PositiveIntegerField(blank=True, default=0)
    number_of_periods = models.PositiveIntegerField(blank=True, default=0)
    annual_carrying = models.PositiveIntegerField(blank=True, default=0)
    owner = models.ForeignKey(Usuario, related_name='inv_files', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    removed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date', 'title']
        verbose_name = 'InvFile'
        verbose_name_plural = 'InvFiles'

    def __str__(self):
        return self.title


# Model for Inventory Status item.
class InvItem(models.Model):
    part_number = models.CharField(max_length=12)
    safe_stock = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    on_hand = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    past_due = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    receipts = models.CharField(max_length=250, blank=True, null=True)
    order = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    file = models.ForeignKey(InvFile, related_name='inv_items', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_date = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['file', 'order']
        verbose_name = 'InvItem'
        verbose_name_plural = 'InvItems'

    def __str__(self):
        return f"File: {self.file}, Part Number: {self.part_number}"


# Model for Item Master fle.
class ItemMasterFile(models.Model):
    title = models.CharField(max_length=50, default="Untitled")
    number_of_items = models.PositiveIntegerField(blank=True, default=1)
    owner = models.ForeignKey(Usuario, related_name='item_master_files', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    removed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date', 'title']
        verbose_name = 'ItemMasterFile'
        verbose_name_plural = 'ItemMasterFiles'

    def __str__(self):
        return self.title


# Model for Item Master item.
class ItemMaster(models.Model):
    LOT_SIZE_CHOICES = [
        ('LFL', 'LFL'), ('FP', 'FP'), ('FQ', 'FQ'), ('EOQ', 'EOQ')
    ]
    part_number = models.CharField(max_length=12)
    clase = models.CharField(max_length=50, blank=True, null=True, default=None)
    lot_size = models.CharField(max_length=5, choices=LOT_SIZE_CHOICES, default="LFL")
    multiple = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    lead_time = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    yield_percent = models.DecimalField(default=0, max_digits=4, decimal_places=3, validators=[MaxValueValidator(1), MinValueValidator(0)])
    unit_value = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    order_cost = models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    carrying_cost = models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    demand = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    file = models.ForeignKey(ItemMasterFile, related_name='items_masters', on_delete=models.CASCADE)
    order = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_date = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['file', 'order']
        verbose_name = 'ItemMaster'
        verbose_name_plural = 'ItemMasters'

    def __str__(self):
        return f"File: {self.file}, Part Number: {self.part_number}"


# Model for report.
class Report(models.Model):
    title = models.CharField(max_length=50, default="Untitled Report")
    owner = models.ForeignKey(Usuario, related_name='reports', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    removed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date', 'title']
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'

    def __str__(self):
        return self.title

# Model for report item.
class ReportItem(models.Model):
    LOT_SIZE_CHOICES = [
        ('LFL', 'LFL'), ('FP', 'FP'), ('FQ', 'FQ'), ('EOQ', 'EOQ')
    ]
    part_number = models.CharField(max_length=12)
    yield_percent = models.DecimalField(default=0, max_digits=4, decimal_places=3, validators=[MaxValueValidator(1), MinValueValidator(0)])
    lead_time = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    order_cost = models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    parent = models.CharField(max_length=12, blank=True, null=True)
    carrying_cost = models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    qty = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0)])
    lot_size = models.CharField(max_length=5, choices=LOT_SIZE_CHOICES, default="LFL")
    safe_stock = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    factor = models.CharField(max_length=30, null=True, blank=True)
    on_hand = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    report = models.ForeignKey(Report, related_name='items', on_delete=models.CASCADE)
    order = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_date = models.DateTimeField(default=datetime.now)
    removed = models.BooleanField(default=False)

    class Meta:
        ordering = ['report', 'order']
        verbose_name = 'ReportItem'
        verbose_name_plural = 'ReportItems'

    def __str__(self):
        return f"Report: {self.report}, Part Number: {self.part_number}"


# Model for item period in report.
class ReportPeriod(models.Model):
    period = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    gross_requirement = models.IntegerField(default=0)
    receipt = models.IntegerField(default=0)
    on_hand = models.IntegerField(default=0)
    net_requirement = models.IntegerField(default=0)
    item = models.ForeignKey(ReportItem, related_name='periods', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_date = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['item', 'period']
        verbose_name = 'ReportPeriod'
        verbose_name_plural = 'ReportPeriods'

    def __str__(self):
        return f"Item: {self.item}, Period: {self.period}"