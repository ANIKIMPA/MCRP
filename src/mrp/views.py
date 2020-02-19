from .models import BomFile, Item, MastFile, Period
from .serializers import BomFileSerializer, ItemSerializer, MastFileSerializer, PeriodSerializer
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
    def get_items(self, request, file_id):
        queryset = Item.objects.all().filter(file=file_id)
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MastFileViewSet(viewsets.ModelViewSet):
    queryset = MastFile.objects.all()
    serializer_class = MastFileSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def get_periods(self, request, file_id):
        queryset = Period.objects.filter(file=file_id)
        serializer = PeriodSerializer(queryset, many=True)
        return Response(serializer.data)
