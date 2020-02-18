from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginLevelViewSet

router = DefaultRouter()
router.register(r'users', LoginLevelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
