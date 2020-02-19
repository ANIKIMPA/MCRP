from django.contrib import admin
from .models import Item, BomFile, MastFile, Period

# Register your models here.
class BomFileAdmin(admin.ModelAdmin):
    pass

class ItemAdmin(admin.ModelAdmin):
    pass

class MastFileAdmin(admin.ModelAdmin):
    pass
class PeriodAdmin(admin.ModelAdmin):
    pass

admin.site.register(BomFile, BomFileAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(MastFile, MastFileAdmin)
admin.site.register(Period, PeriodAdmin)