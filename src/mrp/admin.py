from django.contrib import admin
from .models import Item, File, Period

# Register your models here.
class FileAdmin(admin.ModelAdmin):
    pass

class ItemAdmin(admin.ModelAdmin):
    pass

class PeriodAdmin(admin.ModelAdmin):
    pass

admin.site.register(File, FileAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Period, PeriodAdmin)