# from rest_framework import routers
# from .viewsets import FileViewSet, ItemViewSet

# router = routers.SimpleRouter()
# router.register("files", FileViewSet)
# router.register("files", ItemViewSet)

# urlpatterns = router.urls

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

file_items = views.FileViewSet.as_view({
    'get': 'get_items'
})

file_masters_schedules = views.PeriodViewSet.as_view({
    'get': 'get_masters_schedules'
})

router = DefaultRouter()
router.register(r'files', views.FileViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'periods', views.PeriodViewSet)

urlpatterns = [
    path('files/<int:file_id>/items', file_items, name='file-items'),
    path('files/<int:file_id>/periods', file_masters_schedules, name='file-periods'),
    path('', include(router.urls)),
]
