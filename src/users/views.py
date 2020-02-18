from .models import LoginLevel
from .serializers import LoginLevelSerializer
from rest_framework import viewsets


class LoginLevelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LoginLevel.objects.all().order_by('-date_joined')
    serializer_class = LoginLevelSerializer
