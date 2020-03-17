from django.urls import path
from .views import UserRegistrationView, UserLoginView, ProfileView

urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('profile/', ProfileView.as_view()),
]
