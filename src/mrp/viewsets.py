from rest_framework import permissions
from .models import BomItem, File
from .serializers import FileSerializer, BomItemSerializer
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
# from rest_framework.decorators import action


# @api_view(['GET'])
# def api_root(request):
#     return Response({
#         'users': reverse('user-list', request=request),
#         'files': reverse('file-list', request=request)
#     })


class FileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # def highlight(self, request, *args, **kwargs):
    #     snippet = self.get_object()
    #     return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# class ItemList(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def get(self, request):
#         items = BomItem.objects.all()
#         serializer = BomItemSerializer(items, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = BomItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def perform_create(self, file):
#         file.save(owner=self.request.user)


# class ItemDetail(APIView):
#     """
#     Retrieve, update or delete a code file.
#     """
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def get_object(self, pk):
#         try:
#             file = BomItem.objects.get(pk=pk)
#         except BomItem.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         file = self.get_object(pk)
#         serializer = BomItemSerializer(file)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         file = self.get_object(pk)
#         serializer = BomItemSerializer(file, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         file = self.get_object(pk)
#         file.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
