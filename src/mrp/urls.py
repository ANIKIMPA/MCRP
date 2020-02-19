# from rest_framework import routers
# from .viewsets import FileViewSet, ItemViewSet

# router = routers.SimpleRouter()
# router.register("files", FileViewSet)
# router.register("files", ItemViewSet)

# urlpatterns = router.urls

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

file_items = views.BomFileViewSet.as_view({
    'get': 'get_items'
})

file_periods = views.PeriodViewSet.as_view({
    'get': 'get_periods'
})

router = DefaultRouter()
router.register(r'bom-files', views.BomFileViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'mast-files', views.MastFileViewSet)
router.register(r'periods', views.PeriodViewSet)

urlpatterns = [
    path('bom-files/<int:file_id>/items', file_items, name='file-items'),
    path('mast-files/<int:file_id>/periods', file_periods, name='file-periods'),
    path('', include(router.urls)),
]
