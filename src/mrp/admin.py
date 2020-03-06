from django.contrib import admin
from .models import (
    BomItem, BomFile, MastFile, MastItem,
    InvFile,
    InvItem,
    ItemMasterFile,
    ItemMaster,
)

# Register your models here.
class BomFileAdmin(admin.ModelAdmin):
    pass

class BomItemAdmin(admin.ModelAdmin):
    pass

class MastFileAdmin(admin.ModelAdmin):
    pass
class MastItemAdmin(admin.ModelAdmin):
    pass

class InvFileAdmin(admin.ModelAdmin):
    pass
class InvItemAdmin(admin.ModelAdmin):
    pass

class ItemMasterFileAdmin(admin.ModelAdmin):
    pass
class ItemMasterAdmin(admin.ModelAdmin):
    pass


admin.site.register(BomFile, BomFileAdmin)
admin.site.register(BomItem, BomItemAdmin)
admin.site.register(MastFile, MastFileAdmin)
admin.site.register(MastItem, MastItemAdmin)
admin.site.register(InvFile, InvFileAdmin)
admin.site.register(InvItem, InvItemAdmin)
admin.site.register(ItemMasterFile, ItemMasterFileAdmin)
admin.site.register(ItemMaster, ItemMasterAdmin)