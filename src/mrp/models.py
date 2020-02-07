from django.db import models
from django.utils.timezone import now

# Create your models here.
class Item(models.Model):
    part_number = models.CharField(max_length=12, blank=True, null=True)
    tipo = models.CharField(max_length=20, blank=True, null=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    qty = models.PositiveIntegerField(blank=True, default=1)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['part_number']
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.part_number