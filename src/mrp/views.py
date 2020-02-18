from .models import File, Item, MasterSchedule
from .serializers import FileSerializer, ItemSerializer, MasterScheduleSerializer
from rest_framework.response import Response
from rest_framework import permissions, viewsets
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework import status


class FileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer
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


class MasterScheduleViewSet(viewsets.ModelViewSet):
    queryset = MasterSchedule.objects.all()
    serializer_class = MasterScheduleSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request):
        queryset = MasterSchedule.objects.filter(file=6)
        serializer = MasterScheduleSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MasterScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def get_masters_schedules(self, request, file_id):
        queryset = MasterSchedule.objects.filter(file=file_id)
        serializer = MasterScheduleSerializer(queryset, many=True)
        return Response(serializer.data)
