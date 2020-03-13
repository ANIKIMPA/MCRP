from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet

router = DefaultRouter()
router.register(r'users', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
