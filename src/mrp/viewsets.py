from rest_framework import viewsets, permissions
from .models import Item, File
from .serializer import FileSerializer, ItemSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)