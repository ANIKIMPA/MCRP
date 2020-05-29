from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

file_bom_items = views.BomItemViewSet.as_view({
    'get': 'get_bom_items'
})

file_mast_items = views.MastItemViewSet.as_view({
    'get': 'get_mast_items'
})
file_inv_items = views.InvItemViewSet.as_view({
    'get': 'get_inv_items'
})
file_items_masters = views.ItemMasterViewSet.as_view({
    'get': 'get_items_masters'
})

router = DefaultRouter()
router.register(r'bom-files', views.BomFileViewSet)
router.register(r'bom-items', views.BomItemViewSet)
router.register(r'mast-files', views.MastFileViewSet)
router.register(r'mast-items', views.MastItemViewSet)

router.register(r'inv-files', views.InvFileViewSet)
router.register(r'inv-items', views.InvItemViewSet)
router.register(r'item-master-files', views.ItemMasterFileViewSet)
router.register(r'items-masters', views.ItemMasterViewSet)

router.register(r'reports', views.ReportViewSet)

# Dynamic urls
urlpatterns = [
    path('bom-files/<int:file_id>/bom-items', file_bom_items, name='file-bom-items'),
    path('mast-files/<int:file_id>/mast-items', file_mast_items, name='file-mast-items'),
    path('inv-files/<int:file_id>/inv-items', file_inv_items, name='file-inv-items'),
    path('item-master-files/<int:file_id>/items-masters', file_items_masters, name='file-items-masters'),
    path('', include(router.urls)),
]
