from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet

register = UsuarioViewSet.as_view({
    'post': 'register'
})

router = DefaultRouter()
router.register(r'users', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register, name="register"),
]
