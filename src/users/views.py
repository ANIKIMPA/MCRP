from .models import LoginLevel
from rest_framework import viewsets
from .serializers import LoginLevelSerializer

class LoginLevelViewSet(viewsets.ModelViewSet):
    queryset = LoginLevel.objects.all().order_by('-date_joined')
    serializer_class = LoginLevelSerializer
