from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().order_by('-date_joined')
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'])
    def register(self, request):
        form = RegistrationForm(request.data)
        if form.is_valid():
            serializer = UsuarioSerializer(request.data)
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            auth = authenticate(email=email, password=password)
            login(request, auth)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
