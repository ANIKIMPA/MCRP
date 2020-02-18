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

file_masters_schedules = views.MasterScheduleViewSet.as_view({
    'get': 'get_masters_schedules'
})

router = DefaultRouter()
router.register(r'files', views.FileViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'masters-schedules', views.MasterScheduleViewSet)

urlpatterns = [
    path('files/<int:file_id>/items', file_items, name='file-items'),
    path('files/<int:file_id>/masters-schedules', file_masters_schedules, name='file-masters-schedules'),
    path('', include(router.urls)),
]
