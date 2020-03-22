from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    UserProfileView,
    UserRegistrationView,
    UserLoginView,
    LogoutAndBlacklistRefreshTokenForUserView
)

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('profile/', UserProfileView.as_view()),
    path('register/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('logout/', LogoutAndBlacklistRefreshTokenForUserView.as_view())
]
