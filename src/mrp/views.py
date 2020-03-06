from .models import (
    BomFile, BomItem, MastFile, MastItem, InvFile, InvItem, ItemMasterFile, ItemMaster
)
from .serializers import (
    BomFileSerializer,
    ItemSerializer,
    MastFileSerializer,
    MastItemSerializer,
    InvFileSerializer,
    InvItemSerializer,
    ItemMasterFileSerializer,
    ItemMasterSerializer,
)
from rest_framework.response import Response
from rest_framework import permissions, viewsets
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework import status


class BomFileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = BomFile.objects.all()
    serializer_class = BomFileSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    @action(detail=True, methods=['get'])
    def get_bom_items(self, request, file_id):
        queryset = BomItem.objects.all().filter(file=file_id)
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = BomItem.objects.all()
    serializer_class = ItemSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MastFileViewSet(viewsets.ModelViewSet):
    queryset = MastFile.objects.all()
    serializer_class = MastFileSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class MastItemViewSet(viewsets.ModelViewSet):
    queryset = MastItem.objects.all()
    serializer_class = MastItemSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def get_mast_items(self, request, file_id):
        queryset = MastItem.objects.filter(file=file_id)
        serializer = MastItemSerializer(queryset, many=True)
        return Response(serializer.data)

class InvFileViewSet(viewsets.ModelViewSet):
    queryset = InvFile.objects.all()
    serializer_class = InvFileSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class InvItemViewSet(viewsets.ModelViewSet):
    queryset = InvItem.objects.all()
    serializer_class = InvItemSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def get_inv_items(self, request, file_id):
        queryset = InvItem.objects.filter(file=file_id)
        serializer = InvItemSerializer(queryset, many=True)
        return Response(serializer.data)


class ItemMasterFileViewSet(viewsets.ModelViewSet):
    queryset = ItemMasterFile.objects.all()
    serializer_class = ItemMasterFileSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class ItemMasterViewSet(viewsets.ModelViewSet):
    queryset = ItemMaster.objects.all()
    serializer_class = ItemMasterSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def get_items_masters(self, request, file_id):
        queryset = ItemMaster.objects.filter(file=file_id)
        serializer = ItemMasterSerializer(queryset, many=True)
        return Response(serializer.data)
