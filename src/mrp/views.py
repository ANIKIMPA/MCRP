from datetime import datetime
from .models import (
    BomFile, BomItem, MastFile, MastItem, InvFile, InvItem, ItemMasterFile, ItemMaster
)
from .serializers import (
    BomFileSerializer,
    BomItemSerializer,
    MastFileSerializer,
    MastItemSerializer,
    InvFileSerializer,
    InvItemSerializer,
    ItemMasterFileSerializer,
    ItemMasterSerializer,
)
from rest_framework.response import Response
from rest_framework import permissions, viewsets, status
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action


class BomFileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = BomFile.objects.filter(removed=0)
    serializer_class = BomFileSerializer
    # authentication_class = (JSONWebTokenAuthentication,)
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class BomItemViewSet(viewsets.ModelViewSet):
    queryset = BomItem.objects.all()
    serializer_class = BomItemSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request):
        now = datetime.now()
        items = []
        for i in range(0, int(request.data["items_number"])):
            items.append(BomItem(
                part_number="-",
                tipo="MAT",
                qty=1,
                file=BomFile.objects.get(pk=request.data["file"]),
                created_date=now
            ))

        bomItems = BomItem.objects.bulk_create(items)
        bomItems = BomItem.objects.filter(created_date=now)
        serializer = BomItemSerializer(bomItems, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['get'])
    def get_bom_items(self, request, file_id):
        queryset = BomItem.objects.all().filter(file=file_id).exclude(file__removed=1)
        serializer = BomItemSerializer(queryset, many=True)
        return Response(serializer.data)


class MastFileViewSet(viewsets.ModelViewSet):
    queryset = MastFile.objects.filter(removed=0)
    serializer_class = MastFileSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class MastItemViewSet(viewsets.ModelViewSet):
    queryset = MastItem.objects.all()
    serializer_class = MastItemSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request):
        now = datetime.now()
        items = []
        for i in range(0, int(request.data["items_number"])):
            items.append(MastItem(
                part_number=request.data["part_numbers"][i],
                periods=request.data["periods"],
                order=request.data["order"] if "order" in request.data else i,
                file=MastFile.objects.get(pk=request.data["file"]),
                created_date=now
            ))

        mastItems = MastItem.objects.bulk_create(items)
        mastItems = MastItem.objects.filter(created_date=now)
        serializer = MastItemSerializer(mastItems, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get'])
    def get_mast_items(self, request, file_id):
        queryset = MastItem.objects.filter(
            file=file_id).exclude(file__removed=1)
        serializer = MastItemSerializer(queryset, many=True)
        return Response(serializer.data)


class InvFileViewSet(viewsets.ModelViewSet):
    queryset = InvFile.objects.filter(removed=0)
    serializer_class = InvFileSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class InvItemViewSet(viewsets.ModelViewSet):
    queryset = InvItem.objects.all()
    serializer_class = InvItemSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request):
        now = datetime.now()
        items = []
        for i in range(0, int(request.data["items_number"])):
            items.append(InvItem(
				part_number = request.data["part_numbers"][i],
				safe_stock = 0,
				on_hand = 0,
				past_due = 0,
				receipts = request.data["receipts"],
				order=request.data["order"] if "order" in request.data else i,
                file=InvFile.objects.get(pk=request.data["file"]),
                created_date=now
            ))

        invItems = InvItem.objects.bulk_create(items)
        invItems = InvItem.objects.filter(created_date=now)
        serializer = InvItemSerializer(invItems, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get'])
    def get_inv_items(self, request, file_id):
        queryset = InvItem.objects.filter(
            file=file_id).exclude(file__removed=1)
        serializer = InvItemSerializer(queryset, many=True)
        return Response(serializer.data)


class ItemMasterFileViewSet(viewsets.ModelViewSet):
    queryset = ItemMasterFile.objects.filter(removed=0)
    serializer_class = ItemMasterFileSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class ItemMasterViewSet(viewsets.ModelViewSet):
    queryset = ItemMaster.objects.all()
    serializer_class = ItemMasterSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request):
        now = datetime.now()
        items = []
        for i in range(0, int(request.data["items_number"])):
            items.append(ItemMaster(
                part_number = request.data["part_numbers"][i],
                lot_size = "LFL",
                multiple = 0,
                lead_time = 0,
                yield_percent = 0,
                unit_value = 0,
                order_cost = 0,
                carrying_cost = 0,
                demand = 0,
                order = request.data["order"] if "order" in request.data else i,
                file = ItemMasterFile.objects.get(pk=request.data["file"]),
                created_date = now
            ))

        itemsMasters = ItemMaster.objects.bulk_create(items)
        itemsMasters = ItemMaster.objects.filter(created_date=now)
        serializer = ItemMasterSerializer(itemsMasters, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get'])
    def get_items_masters(self, request, file_id):
        queryset = ItemMaster.objects.filter(
            file=file_id).exclude(file__removed=1)
        serializer = ItemMasterSerializer(queryset, many=True)
        return Response(serializer.data)
