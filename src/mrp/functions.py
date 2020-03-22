from rest_framework.response import Response
from rest_framework import status


def current_user_files(user, modelFile):
    """
    This view should return a list of all the files
    created by the currently authenticated user.
    """
    return modelFile.objects.filter(owner=user).exclude(removed=1)


def create_file(request, fileSerializer):
    serializer = fileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def current_user_items(user, modelFile, modelItem):
    """
    This view should return a list of all the items
    created by the currently authenticated user.
    """
    files = modelFile.objects.filter(owner=user).exclude(removed=1)
    return modelItem.objects.filter(file__in=files)


def items_in_file(modelItem, file, user, itemSerializer):
    queryset = modelItem.objects.all().filter(file=file).exclude(
        file__removed=1).filter(file__owner=user)
    serializer = itemSerializer(queryset, many=True)
    return Response(serializer.data)
