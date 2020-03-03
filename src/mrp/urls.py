# from rest_framework import routers
# from .viewsets import FileViewSet, ItemViewSet

# router = routers.SimpleRouter()
# router.register("files", FileViewSet)
# router.register("files", ItemViewSet)

# urlpatterns = router.urls

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

file_bom_items = views.BomFileViewSet.as_view({
    'get': 'get_bom_items'
})

file_periods = views.PeriodViewSet.as_view({
    'get': 'get_periods'
})
file_inv_items = views.InvItemViewSet.as_view({
    'get': 'get_inv_items'
})
file_items_masters = views.ItemMasterViewSet.as_view({
    'get': 'get_items_masters'
})

router = DefaultRouter()
router.register(r'bom-files', views.BomFileViewSet)
router.register(r'bom-items', views.ItemViewSet)
router.register(r'mast-files', views.MastFileViewSet)
router.register(r'periods', views.PeriodViewSet)

router.register(r'inv-files', views.InvFileViewSet)
router.register(r'inv-items', views.InvItemViewSet)
router.register(r'item-master-files', views.ItemMasterFileViewSet)
router.register(r'items-masters', views.ItemMasterViewSet)

urlpatterns = [
    path('bom-files/<int:file_id>/bom-items', file_bom_items, name='file-bom-items'),
    path('mast-files/<int:file_id>/periods', file_periods, name='file-periods'),
    path('inv-files/<int:file_id>/inv-items', file_inv_items, name='file-inv-items'),
    path('item-master-files/<int:file_id>/items-masters', file_items_masters, name='file-items-masters'),
    path('', include(router.urls)),
]
